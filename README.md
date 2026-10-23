# HC Falcons Brixen – visueller Prototyp

Astro-Onepager mit zwei Designrichtungen und deutschen sowie italienischen Inhalten.

## Lokal starten

Node.js 22.12+ (oder 24+) und npm verwenden.

```sh
npm ci --cache /tmp/falcons-npm-cache
npm run dev
```

Routen: `/de/dark/`, `/de/clean/`, `/it/dark/`, `/it/clean/`. `/` zeigt die deutsche Dark-Variante. Dark Athletic ist die ausgewählte Hauptvariante. Clean Athletic bleibt unter den direkten Routen als Referenz verfügbar. DE/IT wechselt die Sprache. Es wird kein JavaScript an den Browser ausgeliefert; FAQ und Navigation funktionieren nativ.

```sh
npm run build
npm run preview
```

`dist/` enthält die statische Website und kann später auf Plesk im Dokumentenverzeichnis bereitgestellt werden. Auf dem Plesk-Live-Server wurde nichts veröffentlicht.

## Inhalte und offene Angaben

Alle Texte: `src/data/content.ts`. Gemeinsamer Aufbau: `src/components/Site.astro`. Gestaltung: `src/components/styles.css`. Responsive Bildausgabe: `src/components/Photo.astro`.

Das Original-Logo und sieben Originalfotos wurden über GitHub bereitgestellt und sind eingebunden. Die Zuordnung sowie deutsche und italienische Alternativtexte stehen in `src/data/media.ts`. `src/components/Photo.astro` erzeugt responsive WebP-Bilder über Astro Image; nur das Hero-Bild wird priorisiert, weitere Fotos laden verzögert. Das transparente Original-Logo erscheint in Header und Footer. Die hochgeladenen Originaldateien im Repository-Hauptverzeichnis bleiben unverändert und werden nicht als große Originaldateien an Browser ausgeliefert.

Bestätigte Angaben zu Einstieg, Saison, Hockeyschool, Ausrüstungsleihe, Jugendkategorien, Elternbetreuung und Kontakt sind in beiden Sprachen eingepflegt. Konkrete Kurstermine und Beiträge werden im bestehenden Anmeldeportal ausgewiesen. Noch offen für die finale Veröffentlichung: weitere Sponsoren, Social-Media-Adressen sowie vollständige Rechts- und Datenschutzangaben. Keine konkreten Trainingszeiten, Schnupper- oder Leihgebühren und keine Qualifikationen des Trainerteams wurden ergänzt. Es gibt bewusst kein funktionsloses Kontaktformular und keine erfundenen Kontaktdaten. Die italienischen Texte sind ein erster redaktioneller Entwurf und sollten vor Veröffentlichung geprüft werden.

Schriften (League Spartan und Roboto) werden aus den freien Fontsource-Paketen lokal eingebunden. Keine externen Fontdienste, Tracker, kostenpflichtigen Komponenten oder Laufzeitdienste. Die interne Vorschau verwendet `noindex, nofollow`; das ersetzt keinen Zugriffsschutz. Vor einer späteren Veröffentlichung finale Inhalte, Bildrechte, Rechtsangaben, Domain/Canonical- und hreflang-URLs ergänzen und die Indexierungsregel gezielt anpassen.

## Durchgeführte Validierung

Produktionsbuild mit fünf statischen Seiten erfolgreich. Der überarbeitete Einstieg wurde in beiden Sprachen in Chromium bei 320, 375, 768, 1024 und 1440 Pixeln geprüft: HTTP 200, eine Hauptüberschrift, acht bedienbare FAQ-Einträge, vorhandene Ankerziele und kein horizontaler Überlauf. Sprachwechsel geprüft; die statische Ausgabe enthält keine Script-Tags. Die Browserprüfungen ersetzen noch keinen vollständigen Barrierefreiheits-Audit oder eine Prüfung auf echten Mobilgeräten.

## GitHub-Pages-Vorschau

Der Workflow `.github/workflows/pages.yml` baut bei Push auf `main` und veröffentlicht über GitHub Pages. In GitHub unter **Settings → Pages → Build and deployment → Source** die Option **GitHub Actions** auswählen. Falls der erste Lauf vor Aktivierung fehlschlägt, unter **Actions** den Workflow **Deploy prototype to GitHub Pages** erneut ausführen.

Die vorgesehene Vorschauadresse lautet `https://olennonsgenk86.github.io/falcons_website/`; sie ist erst nach erfolgreichem Deployment erreichbar. Die Sprachlinks berücksichtigen den Projekt-Unterpfad. Lokal bleibt der Basispfad `/`. GitHub Pages stellt die Vorschau öffentlich bereit; `noindex` verhindert keinen direkten Zugriff.

Anmeldeportal und JAKO-Shop sind mit den bestätigten URLs verbunden.

Zum Prüfen des Pages-Builds: `GITHUB_PAGES=true npm run build`. Für Plesk weiterhin ohne diese Variable bauen.

## Anmeldungen und Shop

Die bestätigten externen URLs werden zentral in `src/data/links.ts` gepflegt. Die Auswahl „Eislaufen lernen“ / „Mit Eishockey starten“ steht direkt hinter dem Hero unter `#angebote`. Hero- und Header-Buttons „Jetzt anmelden“ führen dorthin. Die deutsche Einstiegsbotschaft lautet „Kleine Falken. Große Leidenschaft.“. Kurs- und Kategorieanmeldungen führen ins bestehende Registrix-Portal; Probetraining und Rückfragen an `mailto:info@hc-falcons.it`. Der Shop steht zurückhaltend unterhalb des Kontaktbereichs und im Footer.

Kostenhinweise sind bewusst getrennt: erstes Hockeyschool-Jahr für Kinder unter 8 Jahren kostenlos; Ausrüstungsleihe bis 16 Jahre gegen Gebühr. Für Beträge und aktuelle Kurstermine gilt das Anmeldeportal. Die Werte Bewegung, Freundschaft, Teamgeist und Spaß sind unter „Hier wächst mehr als Können.“ wieder als vier Boxen mit Beschreibung dargestellt. Der separate Saison-/Sommercamp-Block ist entfernt; die bestätigten Saisoninformationen bleiben in den FAQ erhalten. Der Vereinsabschnitt beschreibt den Trainings- und Spielbetrieb aller Jugendkategorien von September bis April.

## Shopvorschau und gemeinsame Einstiegsaktionen

Unter dem praktischen Einstiegsleitfaden stehen genau zwei gemeinsame Aktionen: Anmeldung im Registrix-Portal und E-Mail an den Verein. Die einzelnen Schritte haben keine eigenen Buttons mehr. Der gesonderte Abgrenzungssatz zur Elternbetreuung ist entfernt.

`src/components/Shop.astro` zeigt direkt unter „Einblicke aufs Eis“ einen nativen, per Touch, Trackpad und Tastatur bedienbaren Scroll-Snap-Slider. Kein Autoplay und kein zusätzliches Browser-JavaScript. Alle elf vom Nutzer hochgeladenen Produktbilder werden über `src/data/shop.ts` eingebunden und von Astro als WebP optimiert. Jedes Bild und seine deutsche beziehungsweise italienische Beschriftung führen zum bestätigten JAKO-Falcons-Shop. Die Originale bleiben unverändert. Preise, Modellnamen oder Verfügbarkeiten wurden nicht erfunden.

Die Produktbilder sind nun lokal vorhanden; ein Abruf des Shops zur Laufzeit ist nicht nötig. Die bisherigen Fotoplatzhalter sind entfernt.

## Gemeinsamer Angebotsblock

Die beiden Einstiegswege sind als ein zusammenhängender Bild-Text-Block gestaltet: Originalfoto vom Eislaufenlernen links, zwei durch eine Linie getrennte Informationsbereiche rechts. Auf schmalen Displays steht das Bild über den Angeboten. Alle bestätigten Angaben und Anmelde-/E-Mail-Ziele bleiben erhalten. Texte und Bildunterschrift sind in Deutsch und Italienisch verfügbar.

## Hauptsponsor Spark

Der Bereich unmittelbar vor dem Footer zeigt das vom Nutzer bereitgestellte Spark-Logo mit „Unser Hauptsponsor“ / „Il nostro sponsor principale“. Die RGB-Positivversion aus dem Logo-ZIP liegt unverändert unter `src/assets/sponsors/spark.png`; Astro erzeugt die optimierte Webausgabe. Es wurde keine unbestätigte Sponsor-URL ergänzt. Die bisherigen Partner-Platzhalter sind ersetzt.
