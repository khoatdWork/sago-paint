const { defineConfig } = require('@playwright/test');
module.exports = defineConfig({
  testDir: './tests/browser',
  timeout: 300000,
  expect: { timeout: 10000 },
  workers: 3,
  fullyParallel: true,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: { baseURL: 'http://127.0.0.1:4173', headless: true, trace: 'retain-on-failure' },
  webServer: { command: 'node tools/serve-static.js', url: 'http://127.0.0.1:4173', reuseExistingServer: false },
});
