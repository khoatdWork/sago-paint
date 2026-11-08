const fs = require('node:fs');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '..');
// These are public route/asset directories, never the whole repository.
const PUBLIC_DIRS = ['assets', 'phong-thuy-son-nha', 'tinh-son'];
const PUBLIC_ROOT_FILES = ['sitemap.xml', 'robots.txt', '_redirects', '_headers'];
const isVerification = (file) => /^google[a-z0-9]+\.html$/i.test(path.basename(file));

function publicFiles(root = ROOT) {
  const result = [];
  function visit(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isSymbolicLink()) throw new Error(`Public symlink is not allowed: ${full}`);
      if (entry.isDirectory()) visit(full);
      else if (entry.isFile()) result.push(full);
    }
  }
  for (const entry of fs.readdirSync(root, { withFileTypes: true })) {
    if (entry.isFile() && (/\.(html|css)$/.test(entry.name) || PUBLIC_ROOT_FILES.includes(entry.name))) {
      result.push(path.join(root, entry.name));
    }
  }
  for (const dir of PUBLIC_DIRS) if (fs.existsSync(path.join(root, dir))) visit(path.join(root, dir));
  return result.sort();
}

function pageFiles(root = ROOT) {
  return publicFiles(root).filter(file => file.endsWith('.html') && !isVerification(file));
}

function routeFromFile(file, root = ROOT) {
  const relative = path.relative(root, file).split(path.sep).join('/');
  if (relative === 'index.html') return '/';
  if (relative.endsWith('/index.html')) return `/${relative.slice(0, -10)}`;
  return `/${relative.replace(/\.html$/, '')}`;
}

module.exports = { ROOT, PUBLIC_DIRS, publicFiles, pageFiles, routeFromFile, isVerification };
if (require.main === module) console.log(JSON.stringify(pageFiles().map(file => ({
  file: path.relative(ROOT, file).split(path.sep).join('/'), route: routeFromFile(file)
}))));
