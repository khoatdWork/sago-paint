const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { ROOT, pageFiles, routeFromFile } = require('../../tools/site-files');
const routes = pageFiles().map(file => routeFromFile(file));
const representatives = new Set(['/', '/son-noi-that', '/blog', '/son-nha-moi-xay',
  '/phong-thuy-son-nha/', '/phong-thuy-son-nha/tuoi-1990/', '/tinh-son/',
  '/son-sagopaint-noi-that-lau-chui-hieu-qua-anaclean-be-mat-bong-mo']);

for (const width of [360, 768, 1440]) {
  test(`all 54 pages: typography, layout, images, accessibility at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    const failures = [], rows = [];
    let errors = [];
    page.on('pageerror', error => errors.push(error.message));
    for (const route of routes) {
      errors = [];
      const response = await page.goto(route, { waitUntil: 'networkidle' });
      await page.evaluate(async () => {
        await document.fonts.ready;
        await Promise.all([...document.images].map(img => { img.loading = 'eager'; return img.decode().catch(() => {}); }));
      });
      const state = await page.evaluate(() => ({
        overflow: document.documentElement.scrollWidth > innerWidth + 1,
        bodyFont: getComputedStyle(document.body).fontFamily,
        headingFont: getComputedStyle(document.querySelector('h1')).fontFamily,
        fontToken: getComputedStyle(document.documentElement).getPropertyValue('--font-sans').trim(),
        fontMismatches: [...document.body.querySelectorAll('*')]
          .filter(el => !['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(el.tagName)
            && (el.matches('button, input, select, textarea')
              || [...el.childNodes].some(node => node.nodeType === Node.TEXT_NODE && node.textContent.trim())))
          .filter(el => !getComputedStyle(el).fontFamily.startsWith('"Be Vietnam Pro"'))
          .map(el => ({ tag: el.tagName, id: el.id, className: el.className, font: getComputedStyle(el).fontFamily })),
        fontLoaded: [...document.fonts].some(f => f.family.replace(/["']/g, '') === 'Be Vietnam Pro' && f.status === 'loaded'),
        failedImages: [...document.images].filter(img => img.complete && !img.naturalWidth).map(img => img.src),
        duplicateIds: [...document.querySelectorAll('[id]')].map(el => el.id)
          .filter((id, index, ids) => ids.indexOf(id) !== index),
        skipLink: document.querySelector('body a').getAttribute('href') === '#main-content',
        skipLinkOutsideViewport: document.querySelector('.skip-link').getBoundingClientRect().bottom <= 0,
      }));
      const axe = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']).analyze();
      const violations = axe.violations.filter(v => ['serious', 'critical'].includes(v.impact))
        .map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.map(n => ({ target: n.target, summary: n.failureSummary })) }));
      const problems = [];
      if (response.status() !== 200) problems.push(`HTTP ${response.status()}`);
      if (state.overflow) problems.push('horizontal overflow');
      if (!state.fontLoaded || !state.bodyFont.startsWith('"Be Vietnam Pro"') || !state.headingFont.startsWith('"Be Vietnam Pro"')) problems.push('font not loaded/applied');
      if (!state.fontToken.includes('Be Vietnam Pro') || state.fontMismatches.length) problems.push('undefined font token or inconsistent text/control font');
      if (!state.skipLink) problems.push('skip link missing');
      if (!state.skipLinkOutsideViewport) problems.push('skip link visible before keyboard focus');
      if (state.failedImages.length) problems.push(`failed images: ${state.failedImages.join(', ')}`);
      if (state.duplicateIds.length) problems.push(`duplicate IDs: ${state.duplicateIds.join(', ')}`);
      if (errors.length) problems.push(`page errors: ${errors.join(', ')}`);
      if (violations.length) problems.push(`axe: ${violations.map(v => v.id).join(', ')}`);
      rows.push({ route, width, status: response.status(), ...state, errors: [...errors], violations });
      if (rows.length % 10 === 0) console.log(`${width}px: checked ${rows.length}/54 pages`);
      if (problems.length) failures.push({ route, problems });
      if (representatives.has(route) && width !== 768) {
        const target = path.join(ROOT, 'output/screenshots', `${route.replace(/[^a-z0-9-]/g, '_') || 'home'}-${width}.png`);
        fs.mkdirSync(path.dirname(target), { recursive: true });
        await page.screenshot({ path: target, fullPage: true });
      }
    }
    fs.mkdirSync(path.join(ROOT, 'output'), { recursive: true });
    fs.writeFileSync(path.join(ROOT, `output/browser-${width}.json`), JSON.stringify(rows, null, 2));
    expect(failures).toEqual([]);
  });
}

for (const width of [360, 1440]) {
  test(`skip link stays hidden until keyboard focus in local files at ${width}px`, async ({ page }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.route(/^https?:/, route => route.abort());
    for (const file of pageFiles().filter(file => representatives.has(routeFromFile(file)) || routeFromFile(file) === '/ve-chung-toi')) {
      await page.goto(pathToFileURL(file).href, { waitUntil: 'networkidle' });
      const skip = page.locator('.skip-link');
      await expect(skip).not.toBeInViewport();
      await page.keyboard.press('Tab');
      await expect(skip).toBeFocused();
      await expect(skip).toBeInViewport({ ratio: 1 });
      await page.keyboard.press('Enter');
      await expect(page.locator('#main-content')).toBeFocused();
      await expect(skip).not.toBeInViewport();
    }
  });
}

test('calculator modes, rounding, presets and keyboard tabs', async ({ page }) => {
  await page.goto('/tinh-son/');
  await page.locator('#tab-room').focus();
  await page.keyboard.press('ArrowRight');
  await expect(page.locator('#tab-area')).toBeFocused();
  await expect(page.locator('#tab-room')).toHaveAttribute('tabindex', '-1');
  await page.locator('#manualArea').fill('100');
  await page.locator('#coatsArea').fill('2');
  await expect(page.locator('#paintNeeded')).toHaveText('20 L');
  await expect(page.locator('#bucketResult')).toHaveText('2 thùng 18L');
  await expect(page.locator('#totalCost')).toHaveText('2.550.000 VNĐ');
  await page.locator('#manualArea').fill('0');
  await expect(page.locator('#paintNeeded')).toHaveText('0 L');
  await expect(page.locator('#totalCost')).toHaveText('0 VNĐ');
  await page.locator('#manualArea').fill('91');
  await expect(page.locator('#paintNeeded')).toHaveText('19 L');
  await page.locator('[data-preset="bedroom"]').click();
  await expect(page.locator('#tab-room')).toHaveAttribute('aria-selected', 'true');
  await expect(page.locator('#length')).toHaveValue('4');
  await expect(page.locator('#paintNeeded')).toHaveText('9 L');
  await page.locator('#tab-room').focus();
  await page.keyboard.press('End');
  await expect(page.locator('#tab-area')).toBeFocused();
  await page.keyboard.press('Home');
  await expect(page.locator('#tab-room')).toBeFocused();
  await page.locator('#tab-area').click();
  await page.locator('#manualArea').fill('1e308');
  await expect(page.locator('#calculationMessage')).toContainText('quá lớn');
  await expect(page.locator('#totalCost')).toHaveText('—');
  await page.locator('#manualArea').fill('100');
  await expect(page.locator('#totalCost')).toHaveText('2.550.000 VNĐ');
});

test('consultation validates, opens composed email with estimate and keeps data', async ({ page }) => {
  await page.goto('/tinh-son/');
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect(page.locator('#fullName')).toBeFocused();
  await page.locator('#fullName').fill('Nguyễn An & Bình');
  await page.locator('#phone').fill('0901234567');
  await page.locator('#email').fill('an@example.com');
  await page.locator('#projectType').selectOption({ label: 'Nhà phố' });
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Page.enable');
  let mailto = '';
  cdp.on('Page.frameRequestedNavigation', event => { if (event.url.startsWith('mailto:')) mailto = event.url; });
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect.poll(() => mailto).toContain('mailto:info.sagopaint@gmail.com');
  const url = new URL(mailto);
  expect(url.searchParams.get('body')).toContain('Nguyễn An & Bình');
  expect(url.searchParams.get('body')).toContain('0901234567');
  expect(url.searchParams.get('body')).toContain('VNĐ');
  await expect(page.locator('#formMessage')).toContainText('tự gửi email');
  await expect(page.locator('#fullName')).toHaveValue('Nguyễn An & Bình');
  await expect(page.locator('a[href="tel:+842866815050"]').first()).toBeVisible();
});

test('navigation, skip link and offline font fallback', async ({ page }) => {
  await page.route(/fonts\.(googleapis|gstatic)\.com/, route => route.abort());
  await page.setViewportSize({ width: 360, height: 800 });
  await page.goto('/');
  await page.keyboard.press('Tab');
  await expect(page.locator('.skip-link')).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.locator('#main-content')).toBeFocused();
  await page.locator('.navbar-toggler').click();
  await expect(page.locator('.navbar-collapse')).toHaveClass(/show/);
  await page.locator('header').getByRole('link', { name: 'Nội thất', exact: true }).click();
  await expect(page).toHaveURL(/son-noi-that/);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBe(true);
  await page.goto('/');
  await page.emulateMedia({ reducedMotion: 'reduce' });
  expect(await page.locator('.trend-card').first().evaluate(el =>
    Math.max(...getComputedStyle(el).transitionDuration.split(',').map(parseFloat)))).toBeLessThan(0.01);
});
