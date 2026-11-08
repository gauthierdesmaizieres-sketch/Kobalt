"""Kobalt voice pack: pre-render a protocol's spoken phrases with VoiceStudio (local, PC) into one JSON file.

Usage:  python tools/voicepack.py protocole.txt [--seed 42] [--url http://127.0.0.1:3900]
Then on the phone: Kobalt → « Sprachpaket » → pick the .kobalt-voice.json file.
The keys must equal what index.html speaks exactly (show(): "Schritt N. <step>", plus the fixed DE phrases below).
"""
import argparse, base64, json, re, sys, urllib.request
from pathlib import Path

FIXED = ['Notiert.', 'Timer gestartet.', 'Timer abgelaufen.',
         'Hallo, ich bin die Stimme von Kobalt. Schritt 1: 12,5 g Säure einwiegen.']  # = L.de in index.html
# Spoken form only (the key stays the written text): units read as words, not letters.
UNITS = [(r'(\d)\s*°C\b', r'\1 Grad Celsius'), (r'(\d)\s*mL\b', r'\1 Milliliter'), (r'(\d)\s*µL\b', r'\1 Mikroliter'),
         (r'(\d)\s*mg\b', r'\1 Milligramm'), (r'(\d)\s*kg\b', r'\1 Kilogramm'), (r'(\d)\s*g\b', r'\1 Gramm'),
         (r'(\d)\s*mmol\b', r'\1 Millimol'), (r'(\d)\s*mbar\b', r'\1 Millibar'), (r'(\d)\s*min\b', r'\1 Minuten'),
         (r'(\d)\s*h\b', r'\1 Stunden'), (r'(\d)-mL-', r'\1-Milliliter-')]


def spoken(text):
    for a, b in UNITS:
        text = re.sub(a, b, text)
    return text


def phrases(proto):
    lines = [l.strip() for l in proto.split('\n') if l.strip()]  # same as loadProto()
    return [f'Schritt {i + 1}. {s}' for i, s in enumerate(lines[1:])] + FIXED


def tts(url, text, seed):
    body = json.dumps({'model': 'omnivoice', 'input': spoken(text), 'language': 'de', 'seed': seed,
                       'instruct': 'female, young adult, moderate pitch', 'response_format': 'mp3'}).encode()
    req = urllib.request.Request(url + '/v1/audio/speech', body, {'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=600) as r:
        return r.read()


assert spoken('12,5 g Säure in einen 250-mL-Kolben, 62 °C') == '12,5 Gramm Säure in einen 250-Milliliter-Kolben, 62 Grad Celsius'
assert phrases('Titel\n\n  a \nb')[:2] == ['Schritt 1. a', 'Schritt 2. b']

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('protocol', type=Path)
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--url', default='http://127.0.0.1:3900')
    a = ap.parse_args()
    todo = phrases(a.protocol.read_text(encoding='utf-8'))
    clips = {}
    for n, t in enumerate(todo, 1):
        print(f'{n}/{len(todo)} {t[:60]}', file=sys.stderr)
        clips[t] = base64.b64encode(tts(a.url, t, a.seed)).decode()
    out = a.protocol.with_suffix('.kobalt-voice.json')
    out.write_text(json.dumps({'v': 1, 'type': 'audio/mpeg', 'clips': clips}), encoding='utf-8')
    print(out)
