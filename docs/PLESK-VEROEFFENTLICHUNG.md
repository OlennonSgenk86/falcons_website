# HC Falcons Brixen auf Plesk veröffentlichen

Ziel: **https://www.hc-falcons.it/**. Die neue Website ist statisch; kein WordPress, keine Datenbank und kein Node.js auf dem Server erforderlich.

## 1. Vor dem Austausch sichern

1. In Plesk die Domain **hc-falcons.it** auswählen. Unter den Hosting-Einstellungen das tatsächliche **Dokumentenverzeichnis** ablesen. Häufig heißt es `httpdocs`, es kann aber anders heißen. Nicht in einem Verzeichnis einer anderen Domain arbeiten.
2. Im Plesk-Backup-Manager eine aktuelle Sicherung der Website-Dateien **und der WordPress-Datenbank** erstellen. Eine Kopie herunterladen. Der alte SQL-Export allein ersetzt keine aktuelle vollständige Sicherung mit Bildern und WordPress-Dateien.
3. Die bisherigen Dateien einschließlich versteckter Dateien wie `.htaccess` zusätzlich nachvollziehbar aufbewahren. Backups mit WordPress-Konfiguration oder SQL-Dateien **außerhalb des öffentlich erreichbaren Dokumentenverzeichnisses** ablegen. `.well-known` und von Plesk verwaltete Zertifikatsdateien erhalten.
4. Die alte Datenbank zunächst unverändert behalten. Sie wird von der neuen Website nicht verwendet, ermöglicht aber einen Rückwechsel.

## 2. Dateien austauschen

1. `docs/releases/falcons-website-plesk.zip` von GitHub über **Download raw file** herunterladen.
2. Im Dateimanager die gesicherten WordPress-Dateien aus dem Dokumentenverzeichnis entfernen beziehungsweise in ein Backup **außerhalb des Webroots** verschieben. Nicht ungesichert löschen. Sonst bleiben alte PHP-Dateien und Rewrite-Regeln neben der neuen Website öffentlich erreichbar.
3. Das ZIP in das tatsächliche Dokumentenverzeichnis hochladen und dort entpacken. `index.html` muss direkt in diesem Verzeichnis liegen, **nicht** in einem zusätzlichen Ordner `dist-live` oder `falcons-website-plesk`.
4. Direkt neben `index.html` müssen unter anderem `_astro/`, `it/`, `de/`, `robots.txt`, `sitemap.xml`, `404.html` und `.htaccess` liegen. Versteckte Dateien im Dateimanager anzeigen lassen. Das ZIP danach aus dem öffentlichen Verzeichnis entfernen.
5. Kein SQL importieren, kein WordPress installieren und keine Zugangsdaten in diese Website-Dateien schreiben.

## 3. Domain und HTTPS

- In Plesk ein gültiges SSL-Zertifikat für `hc-falcons.it` **und** `www.hc-falcons.it` aktivieren beziehungsweise das vorhandene prüfen.
- Unter den Hosting-Einstellungen HTTPS aktivieren, HTTP dauerhaft auf HTTPS umleiten und **www** als bevorzugte Domain auswählen.
- `index.html` als Indexdatei verwenden. Die beigelegte `.htaccess` stellt dies für Apache ein. Bei nginx-only muss die entsprechende Index-/Weiterleitungskonfiguration in Plesk beziehungsweise durch Patrick vorgenommen werden; nginx liest keine `.htaccess`.
- Die Domain muss weiterhin auf den richtigen Plesk-Server zeigen. Ein DNS-Wechsel ist nicht erforderlich, wenn der bestehende Hostingplatz verwendet wird.
- Die beigelegte `.htaccess` enthält Weiterleitungen für einige bekannte alte WordPress-Adressen sowie für die bisherigen Power-Play-Vorschaupfade. Zusätzliche alte URLs gegebenenfalls nach Sichtung der bisherigen Website/Logs ergänzen.

## 4. Direkt nach dem Upload prüfen

- `https://www.hc-falcons.it/` – deutsche Startseite
- `https://www.hc-falcons.it/it/` – italienische Startseite, DE/IT-Wechsel in beide Richtungen
- `https://www.hc-falcons.it/de/impressum/` und `/de/datenschutz/`
- `https://www.hc-falcons.it/it/note-legali/` und `/it/privacy/`
- Bilder, Spark-Logo, alle Produktbilder und die Menüpunkte auf Smartphone und Desktop
- Anmeldeportal, Onlineshop, `info@hc-falcons.it`, `+3313779485` und Social-Media-Links
- Alle neun FAQ öffnen; Shop-Slider per Touch oder Tastatur bewegen
- Keine Design-Umschaltleiste, keine Prototyp-Hinweise und kein GitHub-Pages-Hostinghinweis auf der Live-Website
- `https://www.hc-falcons.it/robots.txt` erlaubt Indexierung und nennt die Live-Sitemap; `/sitemap.xml` enthält nur Live-Adressen
- HTTP und die Domain ohne www leiten auf die HTTPS-www-Adresse um

Bei altem Seitenstand Browser mit Strg+F5 beziehungsweise Cmd+Shift+R aktualisieren und gegebenenfalls den Plesk-/Proxy-Cache leeren. Falls die Startseite nicht korrekt erscheint, **noch keine Backups oder alte Datenbank löschen**.

## 5. Rückwechsel bei Problemen

Die neuen statischen Dateien aus dem Dokumentenverzeichnis nehmen und die gesicherten WordPress-Dateien einschließlich der alten `.htaccess` wiederherstellen. Da die Datenbank nicht verändert wurde, bleibt der alte WordPress-Stand verfügbar. Falls über den Backup-Manager wiederhergestellt wird, den passenden vollständigen Sicherungsstand auswählen. Gegebenenfalls den Servercache leeren.

## Paket neu erstellen (Entwicklungsumgebung)

```sh
npm ci --cache /tmp/falcons-npm-cache
npm run build:live
python3 scripts/package-live.py
```

Das ZIP enthält ausschließlich die gebauten öffentlichen Dateien. GitHub-Vorschau und Plesk-Live-Build haben getrennte Pfade und Indexierungsregeln. Die Konfiguration für GitHub Pages bleibt bestehen; sie veröffentlicht nicht auf Plesk.
