const { test, expect } = require('@playwright/test');
const { pathToFileURL } = require('node:url');
const path = require('node:path');
const { ROOT } = require('../../tools/site-files');

for (const file of ['sago-s-68-pro-chong-tham-a-nang-lo-thien-cao-cap.html', 'son-chong-tham-san-thuong-mua-mua.html']) {
  test(`local S68 product image loads in root HTML preview: ${file}`, async ({ page }) => {
    await page.goto(pathToFileURL(path.join(ROOT, file)).href, { waitUntil: 'networkidle' });
    const image = page.locator('img[src$="sago-s68-pro-preview.webp"]').first();
    await image.scrollIntoViewIfNeeded();
    await expect(image).toBeVisible();
    await expect.poll(() => image.evaluate(img => img.complete && img.naturalWidth > 0)).toBe(true);
    const currentSource = await image.evaluate(img => img.currentSrc);
    expect(currentSource.startsWith(pathToFileURL(path.join(ROOT, 'assets/products')).href + '/')).toBe(true);
    expect(currentSource).toMatch(/sago-s68-pro-(?:home|preview)\.webp$/);
  });
}
