const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { ROOT } = require('./site-files');
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.json': 'application/json', '.xml': 'application/xml',
  '.txt': 'text/plain; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.ico': 'image/x-icon',
  '.webmanifest': 'application/manifest+json' };

function createServer(root = path.join(ROOT, 'dist')) {
  root = path.resolve(root);
  const redirectsPath = path.join(root, '_redirects');
  const redirects = fs.existsSync(redirectsPath) ? fs.readFileSync(redirectsPath, 'utf8')
    .split(/\r?\n/).map(l => l.trim()).filter(l => l && !l.startsWith('#')).map(l => l.split(/\s+/)) : [];
  return http.createServer((req, res) => {
    if (!['GET', 'HEAD'].includes(req.method)) { res.writeHead(405); res.end(); return; }
    let route;
    try { route = decodeURIComponent(new URL(req.url, 'http://localhost').pathname); }
    catch { res.writeHead(400); res.end(); return; }
    const redirect = redirects.find(([from]) => from === route);
    if (redirect) { res.writeHead(Number(redirect[2]), { Location: redirect[1] }); res.end(); return; }
    const target = path.resolve(root, `.${route}`);
    if (!target.startsWith(root + path.sep) && target !== root) { res.writeHead(403); res.end(); return; }
    const candidates = [target, `${target}.html`, path.join(target, 'index.html')];
    const file = candidates.find(p => fs.existsSync(p) && fs.statSync(p).isFile());
    if (!file || path.basename(file).startsWith('_') || route.split('/').some(p => p.startsWith('.'))) {
      res.writeHead(404); res.end('Not found'); return;
    }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
    if (req.method === 'HEAD') res.end();
    else fs.createReadStream(file).on('error', () => res.destroy()).pipe(res);
  });
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const port = Number(args.find(x => x.startsWith('--port='))?.slice(7) || 4173);
  const dir = args.find(x => x.startsWith('--dir='))?.slice(6) || 'dist';
  const root = path.resolve(ROOT, dir);
  if (!fs.existsSync(root)) throw new Error('Run npm run build first');
  createServer(root).listen(port, '127.0.0.1', () => console.log(`Serving ${root} at http://127.0.0.1:${port}`));
}
module.exports = { createServer };
