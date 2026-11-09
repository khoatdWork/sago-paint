const { test, expect } = require('@playwright/test');

test('invalid active calculator values block estimates and email; inactive values do not', async ({ page }) => {
  await page.goto('/tinh-son/');
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Page.enable');
  const emails = [];
  cdp.on('Page.frameRequestedNavigation', event => { if (event.url.startsWith('mailto:')) emails.push(event.url); });
  await page.locator('#fullName').fill('Nguyễn An');
  await page.locator('#phone').fill('+84 (90) 123-4567');
  await page.locator('#projectType').selectOption({ label: 'Nhà phố' });
  for (const [id, value] of [['length', '-1'], ['doors', '0.5'], ['coatsRoom', ''], ['coatsRoom', '0']]) {
    await page.locator(`#${id}`).fill(value);
    await expect(page.locator('#totalCost')).toHaveText('—');
    await expect(page.locator(`#${id}`)).toHaveAttribute('aria-invalid', 'true');
    await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
    await expect(page.locator(`#${id}`)).toBeFocused();
    await page.locator(`#${id}`).fill(id === 'coatsRoom' ? '2' : '1');
  }
  await page.locator('#length').fill('');
  await page.locator('#tab-area').click();
  await page.locator('#manualArea').fill('1e309');
  await expect(page.locator('#totalCost')).toHaveText('—');
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect(page.locator('#manualArea')).toBeFocused();
  expect(emails).toEqual([]);
  await page.locator('#manualArea').fill('1e308');
  await expect(page.locator('#calculationMessage')).toContainText('quá lớn');
  await page.locator('#manualArea').fill('0');
  await expect(page.locator('#totalCost')).toHaveText('0 VNĐ');
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect.poll(() => emails.length).toBe(1);
  await page.setViewportSize({ width: 360, height: 900 });
  await page.locator('#manualArea').fill('100000000');
  await expect(page.locator('#totalCost')).not.toHaveText('—');
  const clippedMetrics = await page.locator('.metric-card strong, .cost-card strong').evaluateAll(nodes =>
    nodes.filter(node => {
      const range = document.createRange();
      range.selectNodeContents(node);
      const text = range.getBoundingClientRect();
      const card = node.parentElement.getBoundingClientRect();
      return text.right > card.right + 1 || text.bottom > card.bottom + 1;
    }).map(node => node.id));
  expect(clippedMetrics).toEqual([]);
});

test('contact validation trims names and accepts flexible international phone numbers', async ({ page }) => {
  await page.goto('/tinh-son/');
  const cdp = await page.context().newCDPSession(page);
  await cdp.send('Page.enable');
  const emails = [];
  cdp.on('Page.frameRequestedNavigation', event => { if (event.url.startsWith('mailto:')) emails.push(event.url); });
  await page.locator('#fullName').fill('   ');
  await page.locator('#phone').fill('abc');
  await page.locator('#projectType').selectOption({ label: 'Nhà phố' });
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect(page.locator('#fullName')).toBeFocused();
  await page.locator('#fullName').fill('  Nguyễn An  ');
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect(page.locator('#phone')).toBeFocused();
  expect(emails).toEqual([]);
  await page.locator('#phone').fill('+84 (90) 123-4567');
  expect(await page.locator('#phone').evaluate(el => el.checkValidity())).toBe(true);
  await page.getByRole('button', { name: 'Soạn email tư vấn' }).click();
  await expect.poll(() => emails.length).toBe(1);
  expect(new URL(emails[0]).searchParams.get('body')).toContain('Họ tên: Nguyễn An\n');
  await expect(page.locator('#projectTypeError')).toHaveCount(1);
  expect(await page.locator('#projectType').evaluate(el => document.getElementById(el.getAttribute('aria-describedby')).parentElement.contains(el))).toBe(true);
  for (const id of ['length', 'width', 'height', 'doors', 'windows', 'coatsRoom', 'manualArea', 'coatsArea']) {
    await expect(page.locator(`#${id}`)).toHaveAttribute('aria-describedby', 'calculationMessage');
  }
});


test('calculator and local S68 recommendation work from a local file', async ({ page }) => {
  const path = require('node:path');
  const { pathToFileURL } = require('node:url');
  await page.setViewportSize({ width: 360, height: 800 });
  await page.route(/^https?:/, route => route.abort());
  await page.goto(pathToFileURL(path.resolve(__dirname, '../../tinh-son/index.html')).href);
  await page.locator('#tab-area').click();
  await page.locator('#manualArea').fill('100');
  await expect(page.locator('#paintNeeded')).toHaveText('20 L');
  await page.locator('#paintTypeArea').selectOption({ label: 'Sơn Chống Thấm' });
  const s68 = page.locator('img[alt="SAGO S68 Pro"]');
  expect(await s68.evaluate(async img => { await img.decode(); return img.naturalWidth > 0 && img.src.startsWith('file:'); })).toBe(true);
  await page.locator('#coatsArea').fill('2.5');
  await expect(page.locator('#totalCost')).toHaveText('—');
});
