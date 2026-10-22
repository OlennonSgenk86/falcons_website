import { defineConfig } from 'astro/config';
const pages = process.env.GITHUB_PAGES === 'true';
export default defineConfig({
  output: 'static',
  site: pages ? 'https://olennonsgenk86.github.io' : undefined,
  base: pages ? '/falcons_website' : '/',
  devToolbar: { enabled: false },
});
