import { defineConfig } from 'astro/config';
const live = process.env.SITE_MODE === 'live';
const pages = !live && process.env.GITHUB_PAGES === 'true';
export default defineConfig({
  output: 'static',
  site: live ? 'https://www.hc-falcons.it' : pages ? 'https://olennonsgenk86.github.io' : undefined,
  base: pages ? '/falcons_website' : '/',
  devToolbar: { enabled: false },
});
