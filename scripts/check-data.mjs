import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { dirname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const load = file => JSON.parse(readFileSync(resolve(root, 'data', file), 'utf8'));
const unique = records => {
  const ids = records.map(r => r.id ?? r.slug);
  assert(ids.every(id => typeof id === 'string' && id.length > 0), 'Missing id');
  assert.equal(new Set(ids).size, ids.length, 'Duplicate id');
};
const fileExists = file => {
  assert.equal(typeof file, 'string');
  const target = resolve(root, file);
  assert(target.startsWith(root + sep), `Path leaves repository: ${file}`);
  assert(existsSync(target), `Missing file: ${file}`);
};
const books = load('books.json');
const learning = load('learning.json');
const exercises = load('exercises.json');
const papers = load('papers.json');
for (const data of [books, learning, exercises, papers]) {
  assert.equal(data.schemaVersion, '1.0');
  assert.equal(data.license, 'CC-BY-4.0');
}
unique(books.books);
const chapterFiles = new Set();
for (const book of books.books) {
  fileExists(book.readme); fileExists(book.full); unique(book.chapters);
  for (const chapter of book.chapters) { fileExists(chapter.file); chapterFiles.add(chapter.file); }
}
unique(learning.tracks);
for (const track of learning.tracks) {
  for (const row of track.rows) {
    if (row.handout) fileExists(row.handout);
    assert(row.title && row.task && row.check);
    assert.equal(row.chapters.length, row.chapterFiles.length);
    for (const file of row.chapterFiles) assert(chapterFiles.has(file), `Unknown chapter: ${file}`);
  }
}
unique(exercises.lessons);
for (const lesson of exercises.lessons) {
  fileExists(lesson.handout); unique(lesson.claims); assert(lesson.source.length > 0);
  for (const claim of lesson.claims) {
    assert(Object.hasOwn(exercises.answerValues, claim.answer));
    assert(claim.text && claim.reason);
  }
}
unique(papers.papers);
for (const paper of papers.papers) {
  assert(Number.isInteger(paper.year)); assert(paper.title && paper.zh);
  assert.equal(new URL(paper.url).protocol, 'https:');
  assert(chapterFiles.has(paper.chapterFile));
}
const fields = ['id','name','year','topic','title','zh','author','url','question','finding','explanation','boundary','task','prompt','chapter'];
const quote = value => '"' + String(value ?? '').replaceAll('"','""') + '"';
const expected = fields.map(quote).join(',') + '\n' + papers.papers.map(p => fields.map(f => quote(p[f])).join(',')).join('\n') + '\n';
assert.equal(readFileSync(resolve(root,'data/papers.csv'),'utf8'), expected, 'CSV differs from JSON');
for (const file of ['LICENSE','LICENSES.md','scripts/LICENSE','books/ai-app-dev/examples/LICENSE']) fileExists(file);
const presentations = load('presentations.json');
assert.equal(presentations.schemaVersion, '1.0');
unique(presentations.presentations);
for (const deck of presentations.presentations) {
  assert(Number.isInteger(deck.pages) && deck.pages > 0);
  assert(deck.title && deck.versionLabel && deck.outline.length > 0);
  fileExists(`slides/${deck.id}/README.md`);
  for (const [field, name, magic] of [['pptx','slides.pptx','PK'], ['pdf','slides.pdf','%PDF-'], ['cover','cover.png','\x89PNG']]) {
    const file = deck.files[name];
    assert.equal(file.path, `slides/${deck.id}/${name}`);
    assert.equal(deck[field], '/' + file.path);
    fileExists(file.path);
    const bytes = readFileSync(resolve(root, file.path));
    assert.equal(bytes.subarray(0, magic.length).toString('latin1'), magic, `Invalid file format: ${file.path}`);
    assert.equal(createHash('sha256').update(bytes).digest('hex'), file.sha256, `File hash differs: ${file.path}`);
  }
}
console.log(`Validated ${books.books.length} books, ${chapterFiles.size} chapters, ${learning.tracks.reduce((sum,t)=>sum+t.rows.length,0)} learning units, ${exercises.lessons.reduce((sum,l)=>sum+l.claims.length,0)} exercises, ${papers.papers.length} papers and ${presentations.presentations.length} slide decks.`);
