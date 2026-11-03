package io.github.gauthierdesmaizieres.kobalt;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

// Opens the web app in a Chrome Custom Tab: Android WebView has no speech recognition, Chrome does.
public class Main extends Activity {
  @Override protected void onCreate(Bundle state) {
    super.onCreate(state);
    Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("https://gauthierdesmaizieres-sketch.github.io/Kobalt/?app=1"));
    Bundle extras = new Bundle();
    extras.putBinder("android.support.customtabs.extra.SESSION", null);
    i.putExtras(extras);
    i.putExtra("android.support.customtabs.extra.TOOLBAR_COLOR", 0xFF0D2F7A);
    i.setPackage("com.android.chrome");
    try {
      startActivity(i);
    } catch (ActivityNotFoundException e) {
      i.setPackage(null); // no Chrome: any browser still opens the app
      startActivity(i);
    }
    finish();
  }
}
