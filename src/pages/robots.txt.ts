import { isLive, liveOrigin } from '../data/site';
export function GET() {
  return new Response(isLive ? `User-agent: *\nAllow: /\nSitemap: ${liveOrigin}/sitemap.xml\n` : 'User-agent: *\nDisallow: /\n', { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
}
