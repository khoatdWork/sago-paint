const { test, expect } = require('@playwright/test');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { ROOT } = require('../../tools/site-files');

for (const route of ['phong-thuy-son-nha/index.html', 'phong-thuy-son-nha/menh-kim/index.html', 'phong-thuy-son-nha/tuoi-1990/index.html']) {
  test(`S68 image loads in direct file preview: ${route}`, async ({ page }) => {
    await page.setViewportSize({ width: 360, height: 900 });
    await page.goto(pathToFileURL(path.join(ROOT, route)).href);
    const image = page.locator('.product-packshot img');
    await image.scrollIntoViewIfNeeded();
    await expect.poll(() => image.evaluate(img => img.complete && img.naturalWidth > 0)).toBe(true);
    expect(await image.evaluate(img => img.currentSrc)).toBe(pathToFileURL(path.join(ROOT, 'assets/products/sago-s68-pro-preview.webp')).href);
  });
}
