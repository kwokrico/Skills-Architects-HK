// Structural checks only: behavioural answers require independent evaluation.
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const suite = JSON.parse(fs.readFileSync(path.join(__dirname, 'evals.json'), 'utf8'));
const ids = new Set(), slugs = new Set();
let assertions = 0;
for (const entry of suite.evals) {
  if (!Number.isInteger(entry.id) || entry.id < 1 || ids.has(entry.id)) throw Error(`Invalid/duplicate id: ${entry.id}`);
  ids.add(entry.id);
  if (!entry.slug || slugs.has(entry.slug)) throw Error(`Missing/duplicate slug: ${entry.slug}`);
  slugs.add(entry.slug);
  for (const field of ['prompt', 'expected_output']) {
    if (typeof entry[field] !== 'string' || !entry[field].trim()) throw Error(`Case ${entry.id}: missing ${field}`);
  }
  if (!Array.isArray(entry.assertions) || !entry.assertions.length || entry.assertions.some(a => typeof a !== 'string' || !a.trim())) throw Error(`Case ${entry.id}: invalid assertions`);
  assertions += entry.assertions.length;
  if (!Array.isArray(entry.files)) throw Error(`Case ${entry.id}: files must be an array`);
  for (const file of entry.files) {
    const resolved = path.resolve(root, file);
    if (!resolved.startsWith(root + path.sep) || !fs.statSync(resolved).isFile()) throw Error(`Case ${entry.id}: invalid fixture ${file}`);
  }
}
console.log(`PASS: ${suite.evals.length} unique cases, ${assertions} assertions, all fixtures present. Behaviour not assessed.`);
