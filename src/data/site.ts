export const isLive = process.env.SITE_MODE === 'live';
export const liveOrigin = 'https://www.hc-falcons.it';
export function homePath(lang: 'de'|'it', theme = 'power') {
  const base = import.meta.env.BASE_URL.replace(/\/?$/, '/');
  return isLive ? `${base}${lang === 'it' ? 'it/' : ''}` : `${base}${lang}/${theme}/`;
}
