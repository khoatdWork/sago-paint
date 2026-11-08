const fs = require('node:fs');
const path = require('node:path');
const { ROOT, publicFiles } = require('./site-files');

function build(root = ROOT) {
  const output = path.resolve(root, 'dist');
  if (path.dirname(output) !== path.resolve(root) || path.basename(output) !== 'dist') {
    throw new Error('Build output must stay inside the repository');
  }
  const files = publicFiles(root);
  fs.rmSync(output, { recursive: true, force: true });
  for (const file of files) {
    const target = path.join(output, path.relative(root, file));
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.copyFileSync(file, target);
  }
  console.log(`Built ${files.length} public files in ${output}`);
  return output;
}

if (require.main === module) build();
module.exports = { build };
