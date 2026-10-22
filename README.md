# HC Falcons Brixen – visueller Prototyp

Astro-Onepager mit zwei Designrichtungen und deutschen sowie italienischen Inhalten.

## Lokal starten

Node.js 22.12+ (oder 24+) und npm verwenden.

```sh
npm ci --cache /tmp/falcons-npm-cache
npm run dev
```

Routen: `/de/dark/`, `/de/clean/`, `/it/dark/`, `/it/clean/`. `/` zeigt die deutsche Dark-Variante. Die Vorschauleiste wechselt das Design, DE/IT die Sprache. Es wird kein JavaScript an den Browser ausgeliefert; FAQ und Navigation funktionieren nativ.

```sh
npm run build
npm run preview
```

`dist/` enthält die statische Website und kann später auf Plesk im Dokumentenverzeichnis bereitgestellt werden. Es wurde nichts veröffentlicht.

## Inhalte und offene Angaben

Alle Texte: `src/data/content.ts`. Gemeinsamer Aufbau: `src/components/Site.astro`. Gestaltung: `src/components/styles.css`. Bildplatzhalter: `src/components/Photo.astro`.

Keine Originalfotos oder bisherigen Website-Texte wurden bereitgestellt. Die gezeichneten Eisflächen sind ausdrücklich als Platzhalter beschriftet. Auch das F-Schild ist ein vorläufiges typografisches Markenzeichen, kein offizielles Logo. Für die nächste Phase Originalbilder und Logo unter `src/assets/` ablegen und mit Astros Image-Komponente, sinnvollen Alternativtexten und passenden Ausschnitten einbinden.

Zu bestätigen: Einstiegsalter, Teilnahmevoraussetzungen, Leihmaterial, Trainingsort und -zeiten, Beiträge, Trainer, Vereinskontakt, Anmeldung, Sponsoren, Social-Media-Adressen sowie vollständige Rechts- und Datenschutzangaben. Es gibt bewusst kein funktionsloses Kontaktformular und keine erfundenen Kontaktdaten. Die italienischen Texte sind ein erster redaktioneller Entwurf und sollten vor Veröffentlichung geprüft werden.

Schriften (League Spartan und Roboto) werden aus den freien Fontsource-Paketen lokal eingebunden. Keine externen Fontdienste, Tracker, kostenpflichtigen Komponenten oder Laufzeitdienste. Die interne Vorschau verwendet `noindex, nofollow`; das ersetzt keinen Zugriffsschutz. Vor einer späteren Veröffentlichung finale Inhalte, Bildrechte, Rechtsangaben, Domain/Canonical- und hreflang-URLs ergänzen und die Indexierungsregel gezielt anpassen.

## Durchgeführte Validierung

Produktionsbuild mit fünf statischen Seiten erfolgreich. Beide Sprachen und Designs in Chromium bei 375, 768 und 1440 Pixeln geprüft: HTTP 200, eine Hauptüberschrift, fünf bedienbare FAQ-Einträge, vorhandene Ankerziele und kein horizontaler Überlauf. Design- und Sprachwechsel geprüft; die statische Ausgabe enthält keine Script-Tags. Die Browserprüfungen ersetzen noch keinen vollständigen Barrierefreiheits-Audit oder eine Prüfung auf echten Mobilgeräten.

## GitHub-Pages-Vorschau

Der Workflow `.github/workflows/pages.yml` baut bei Push auf `main` und veröffentlicht über GitHub Pages. In GitHub unter **Settings → Pages → Build and deployment → Source** die Option **GitHub Actions** auswählen. Falls der erste Lauf vor Aktivierung fehlschlägt, unter **Actions** den Workflow **Deploy prototype to GitHub Pages** erneut ausführen.

Die vorgesehene Vorschauadresse lautet `https://olennonsgenk86.github.io/falcons_website/`; sie ist erst nach erfolgreichem Deployment erreichbar. Design- und Sprachwechsel berücksichtigen den Projekt-Unterpfad. Lokal bleibt der Basispfad `/`. GitHub Pages stellt die Vorschau öffentlich bereit; `noindex` verhindert keinen direkten Zugriff.

Zum Prüfen des Pages-Builds: `GITHUB_PAGES=true npm run build`. Für Plesk weiterhin ohne diese Variable bauen.
