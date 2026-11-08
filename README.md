# Kobalt

Protocole de labo mains libres — Laborprotokoll freihändig.

Une page web installable (PWA) qui lit un protocole étape par étape et enregistre les observations dictées avec un horodatage. Français et allemand.

## Utilisation / Verwendung

1. Ouvrir la page dans Chrome sur Android → ⋮ → *Installer l'application*.
2. Coller le protocole : 1ʳᵉ ligne = titre / n° de lot, puis une étape par ligne.
3. Parler :

| FR | DE |
|---|---|
| suivant / précédent / répète | weiter / zurück / wiederholen |
| note … | Notiz … |
| minuteur 10 minutes | Timer 10 Minuten |
| « Kobalt, … » (mode mot d'activation) | „Kobalt, …“ (Aktivierungswort-Modus) |

   Par défaut, le mode **mains libres** écoute en continu : seules les commandes et « note … » / „Notiz …“ sont pris en compte, les bavardages sont ignorés (« okay, weiter » marche aussi). Mode mot d'activation : « Kobalt » seul, puis la commande dans les 8 s. Le menu *Voix* choisit la voix de lecture (la plus naturelle féminine par défaut).

   En **Schweizerdeutsch** : « wiiter », « zrugg », « nomal », « Timer 10 Minute » ; le Hochdeutsch reste compris. Le texte est écrit en allemand standard. Reconnaissance du dialecte à tester : pour les mesures, le Hochdeutsch reste plus sûr.

   **Voix naturelle (pack voix, allemand)** : sur le PC, VoiceStudio ouvert, `python tools/voicepack.py protocole.txt` (même texte que celui collé dans l'app) crée `protocole.kobalt-voice.json`. L'envoyer sur le téléphone, puis *Sprachpaket* dans Kobalt. Les étapes du pack sont lues avec la voix VoiceStudio, le reste avec la voix du téléphone. Modifier une étape = régénérer le pack.

4. Exporter : *Partager* → OneNote, *Copier* → ELN, ou *Tableau CSV* → Excel.
   Les valeurs dictées sont reconnues et mises en colonnes : masse (mg, g, kg), volume (µL, mL, L), quantité (mmol, mol, éq), température (°C), durée (s, min, h), pression (mbar, bar), pH — en français et en allemand („12,5 Gramm“, „62 Grad“).

## Mise en ligne / Veröffentlichen (GitHub Pages)

1. Créer un dépôt vide `Kobalt` sur GitHub.
2. Dans ce dossier :
   ```bash
   git remote add origin https://github.com/<compte>/Kobalt.git
   git push -u origin main
   ```
3. GitHub → *Settings* → *Pages* → *Deploy from a branch* → `main` / `(root)`.
4. Ouvrir `https://<compte>.github.io/Kobalt/` sur le téléphone.

Ouvrir à la voix : « Ok Google, ouvre Kobalt » / „Hey Google, öffne Kobalt“.

## Android (APK)

Si Chrome n'arrive pas à installer l'appli : télécharger `Kobalt.apk` dans les [Releases](https://github.com/gauthierdesmaizieres-sketch/Kobalt/releases), l'ouvrir et autoriser l'installation. L'appli ouvre Kobalt dans Chrome et apparaît comme une appli normale pour Google Assistant et Bixby. Le code du lanceur est dans `android/`.

## iPhone

1. Ouvrir le lien dans **Safari** → bouton Partager ⬆ → **Sur l'écran d'accueil**.
2. Autoriser le micro et la reconnaissance vocale au premier toucher.
3. Ouvrir à la voix : app **Raccourcis** → nouveau raccourci → action **Ouvrir l'URL** (le lien de Kobalt) → le nommer « Kobalt » → « Dis Siri, Kobalt ».

Si le badge indique « non supportée » depuis l'icône de l'écran d'accueil (certaines versions d'iOS), ouvrir Kobalt directement dans Safari : la reconnaissance vocale y fonctionne. Sur iPhone, l'audio est traité par Apple (Siri).

## Confidentialité / Datenschutz

- Les notes restent dans le navigateur du téléphone (localStorage) jusqu'à l'export.
- La reconnaissance vocale est celle de Chrome. Le badge indique si elle tourne **sur l'appareil** ou **dans le cloud (Google)**. Ne pas dicter d'informations confidentielles en mode cloud.
- Brouillon d'observations, pas un enregistrement GxP.

## Fichiers

`index.html` (toute l'appli) · `manifest.webmanifest` · `sw.js` (ouverture hors ligne) · `icon-*.png`
