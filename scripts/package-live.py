"""Package a tested Astro live build; never include repository or database files."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from datetime import datetime
import stat
from hashlib import sha256

root = Path(__file__).resolve().parent.parent
build = root / 'dist-live'
required = ['index.html', 'it/index.html', 'de/impressum/index.html', 'de/datenschutz/index.html', 'it/note-legali/index.html', 'it/privacy/index.html', '404.html', 'robots.txt', 'sitemap.xml']
for name in required:
    if not (build / name).is_file():
        raise SystemExit(f'Missing live output: {name}. Run npm run build:live first.')
for name in ['index.html', 'it/index.html']:
    html = (build / name).read_text()
    for forbidden in ['noindex', 'design-switch', 'Visueller Prototyp', 'Prototipo visivo']:
        if forbidden in html:
            raise SystemExit(f'Preview content in live output: {name}: {forbidden}')
    if 'https://www.hc-falcons.it' not in html:
        raise SystemExit(f'Canonical domain missing: {name}')
if (build / 'designs').exists() or (build / 'de/power').exists():
    raise SystemExit('Design comparison routes must not ship in the live package.')
htaccess = '''# HC Falcons Brixen - static site. HTTPS and preferred www host are configured in Plesk.
DirectoryIndex index.html
ErrorDocument 404 /404.html
<IfModule mod_alias.c>
RedirectMatch 301 ^/home/?$ https://www.hc-falcons.it/
RedirectMatch 301 ^/verein/?$ "https://www.hc-falcons.it/#verein"
RedirectMatch 301 ^/kontakt/?$ "https://www.hc-falcons.it/#kontakt"
RedirectMatch 301 ^/learn-to-skate/?$ "https://www.hc-falcons.it/#angebote"
RedirectMatch 301 ^/impressum/?$ https://www.hc-falcons.it/de/impressum/
RedirectMatch 301 ^/datenschutz/?$ https://www.hc-falcons.it/de/datenschutz/
RedirectMatch 301 ^/de/power/?$ https://www.hc-falcons.it/
RedirectMatch 301 ^/it/power/?$ https://www.hc-falcons.it/it/
</IfModule>
<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
'''
(build / '.htaccess').write_text(htaccess)
files = sorted(p for p in build.rglob('*') if p.is_file())
for file in files:
    if file.suffix.lower() in {'.sql', '.zip', '.php', '.ts', '.astro'}:
        raise SystemExit(f'Unexpected source or server file: {file.name}')
# Astro may emit imported comparison screenshots even for a route with no live paths.
# Exclude only these known preview assets, after verifying they are not referenced.
preview_assets = [p for p in files if p.parent.name == '_astro' and p.name.startswith('Variante-')]
public_markup = '\n'.join(p.read_text() for p in files if p.suffix in {'.html', '.css'})
for file in preview_assets:
    if file.name in public_markup:
        raise SystemExit(f'Preview asset unexpectedly referenced: {file.name}')
files = [p for p in files if p not in preview_assets]
release = root / 'docs/releases/falcons-website-plesk.zip'
release.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(release, 'w', ZIP_DEFLATED) as archive:
    for file in files:
        info = ZipInfo(file.relative_to(build).as_posix(), datetime.fromtimestamp(file.stat().st_mtime).timetuple()[:6])
        info.create_system = 3
        info.external_attr = (stat.S_IFREG | 0o644) << 16
        info.compress_type = ZIP_DEFLATED
        archive.writestr(info, file.read_bytes())
checksum = sha256(release.read_bytes()).hexdigest()
release.with_suffix('.zip.sha256').write_text(f'{checksum}  {release.name}\n')
print(f'Created {release.name}: {len(files)} files, {release.stat().st_size:,} bytes')
print(f'SHA256: {checksum}')
