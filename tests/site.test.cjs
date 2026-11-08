const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { publicFiles, pageFiles, routeFromFile, ROOT } = require('../tools/site-files');
const { build } = require('../tools/build-static');
const { createServer } = require('../tools/serve-static');

test('build contains public files, excludes project instructions, tests, dependencies and stale files', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'sago-build-'));
  try {
    for (const name of ['index.html', 'styles.css', 'AGENTS.md', 'docs/demo.html', '.agents/SKILL.md',
      'tests/fixture.html', 'node_modules/demo.html', 'assets/js/main.js', 'dist/stale.txt']) {
      const file = path.join(root, name); fs.mkdirSync(path.dirname(file), { recursive: true }); fs.writeFileSync(file, name);
    }
    const out = build(root);
    assert.deepEqual(publicFiles(root).map(p => path.relative(root, p)).sort(),
      ['assets/js/main.js', 'index.html', 'styles.css'].map(p => p.split('/').join(path.sep)).sort());
    assert.equal(fs.existsSync(path.join(out, 'AGENTS.md')), false);
    assert.equal(fs.existsSync(path.join(out, 'stale.txt')), false);
    assert.equal(fs.readFileSync(path.join(out, 'index.html'), 'utf8'), 'index.html');
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});

test('public inventory preserves 54 routes and excludes Google verification from pages', () => {
  const routes = pageFiles().map(file => routeFromFile(file));
  assert.equal(routes.length, 54); assert.equal(new Set(routes).size, 54);
  assert.ok(routes.includes('/')); assert.ok(routes.includes('/tinh-son/'));
  assert.ok(routes.includes('/phong-thuy-son-nha/tuoi-1990/'));
  assert.equal(routes.some(route => route.includes('google4bd')), false);
});

test('local server resolves production routes, redirects, HEAD and rejects traversal/private files', async () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'sago-serve-'));
  fs.writeFileSync(path.join(root, 'index.html'), 'home');
  fs.writeFileSync(path.join(root, 'paint.html'), 'paint');
  fs.writeFileSync(path.join(root, '_redirects'), '/old/ /paint 301');
  const server = createServer(root);
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  try {
    assert.equal(await (await fetch(base + '/')).text(), 'home');
    assert.equal(await (await fetch(base + '/paint')).text(), 'paint');
    const redirect = await fetch(base + '/old/', { redirect: 'manual' });
    assert.equal(redirect.status, 301); assert.equal(redirect.headers.get('location'), '/paint');
    assert.equal((await fetch(base + '/paint', { method: 'HEAD' })).status, 200);
    assert.equal((await fetch(base + '/paint', { method: 'POST' })).status, 405);
    assert.equal((await fetch(base + '/_redirects')).status, 404);
    assert.equal((await fetch(base + '/%2e%2e%2fAGENTS.md')).status, 403);
    assert.equal((await fetch(base + '/docs/README.md')).status, 404);
  } finally { await new Promise(resolve => server.close(resolve)); fs.rmSync(root, { recursive: true, force: true }); }
});

test('SEO --check fails on bad metadata without mutating files; cannot deploy', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'sago-seo-'));
  try {
    fs.mkdirSync(path.join(root, 'tools'));
    for (const file of ['seo-sync.js', 'site-files.js']) fs.copyFileSync(path.join(ROOT, 'tools', file), path.join(root, 'tools', file));
    fs.writeFileSync(path.join(root, 'index.html'), '<html><head><title>Test</title></head><body><h1>Home</h1></body></html>');
    const original = fs.readFileSync(path.join(root, 'index.html'));
    const result = spawnSync(process.execPath, ['tools/seo-sync.js', '--check'], { cwd: root, encoding: 'utf8' });
    assert.equal(result.status, 1); assert.match(result.stderr, /missing meta description|missing canonical/);
    assert.deepEqual(fs.readFileSync(path.join(root, 'index.html')), original);
    assert.equal(fs.existsSync(path.join(root, 'sitemap.xml')), false);
    const deploy = spawnSync(process.execPath, ['tools/seo-sync.js', '--check', '--deploy'], { cwd: root, encoding: 'utf8' });
    assert.equal(deploy.status, 1); assert.match(deploy.stderr, /cannot be combined/);
    fs.writeFileSync(path.join(root, 'index.html'), '<html><head><title>Home</title><meta name="description" content="Site description"><link rel="canonical" href="https://sagopaint.vn/wrong"></head><body><h1>Home</h1></body></html>');
    const sync = spawnSync(process.execPath, ['tools/seo-sync.js'], { cwd: root, encoding: 'utf8' });
    assert.equal(sync.status, 0, sync.stderr);
    assert.match(fs.readFileSync(path.join(root, 'index.html'), 'utf8'), /rel="canonical" href="https:\/\/sagopaint.vn\/"/);
  } finally { fs.rmSync(root, { recursive: true, force: true }); }
});
