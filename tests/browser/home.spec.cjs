const { test, expect } = require('@playwright/test');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { ROOT } = require('../../tools/site-files');

for (const width of [360, 768, 1440]) {
  for (const protocol of ['HTTP', 'file']) {
    test(`home S68 image is visible and fits its hero: ${protocol} at ${width}px`, async ({ page }) => {
      await page.setViewportSize({ width, height: 900 });
      await page.goto(protocol === 'HTTP' ? '/' : pathToFileURL(path.join(ROOT, 'index.html')).href,
        { waitUntil: 'networkidle' });
      const image = page.locator('.hero-product-image');
      await expect(image).toHaveCount(1);
      await expect.soft(image).toBeVisible();
      await expect.soft(image).toHaveJSProperty('complete', true);
      const state = await image.evaluate(img => {
        const box = img.getBoundingClientRect();
        const hero = img.closest('.product-hero').getBoundingClientRect();
        return { loaded: img.naturalWidth > 0, width: box.width, height: box.height,
          left: box.left, right: box.right, top: box.top, bottom: box.bottom,
          hero: { left: hero.left, right: hero.right, top: hero.top, bottom: hero.bottom } };
      });
      expect.soft(state.loaded).toBe(true);
      expect.soft(state.width).toBeGreaterThanOrEqual(160);
      expect.soft(state.height).toBeGreaterThanOrEqual(140);
      expect.soft(state.left).toBeGreaterThanOrEqual(Math.max(0, state.hero.left) - 1);
      expect.soft(state.right).toBeLessThanOrEqual(Math.min(width, state.hero.right) + 1);
      expect.soft(state.top).toBeGreaterThanOrEqual(state.hero.top - 1);
      expect.soft(state.bottom).toBeLessThanOrEqual(state.hero.bottom + 1);
    });
  }
}
