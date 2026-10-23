import { isLive, liveOrigin } from '../data/site';
export function GET() {
 const paths = isLive ? ['/', '/it/', '/de/impressum/', '/it/note-legali/', '/de/datenschutz/', '/it/privacy/'] : [];
 return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${paths.map(path => `<url><loc>${liveOrigin}${path}</loc></url>`).join('')}</urlset>`, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
