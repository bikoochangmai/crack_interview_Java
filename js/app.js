'use strict';
const $ = id => document.getElementById(id);
const STORAGE_KEY = 'java-interview-prep-reviewed-v2';
let questions = [];
let reviewed = {};
try { reviewed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch (_) { reviewed = {}; }
const save = () => { try { localStorage.setItem(STORAGE_KEY, JSON.stringify(reviewed)); } catch (_) {} };
const safeCsv = value => '"' + String(value).replace(/"/g, '""').replace(/^[=+@\-\t\r]/, "'") + '"';
function configureLinks() {
  // The canonical repo URL is discovered from the published GitHub Pages URL.
  // A project page uses USER.github.io/REPO/; a user page uses USER.github.io/.
  const host = location.hostname;
  if (!host.endsWith('.github.io')) {
    $('contribute').textContent = 'How to contribute (see README)';
    $('contribute').href = 'https://github.com';
    return;
  }
  const owner = host.slice(0, -'.github.io'.length);
  const project = location.pathname.split('/').filter(Boolean)[0];
  const repo = project && project.toLowerCase() !== 'index.html' ? project : `${owner}.github.io`;
  const root = `https://github.com/${encodeURIComponent(owner)}/${encodeURIComponent(repo)}`;
  $('repo').href = root;
  $('contribute').href = `${root}/edit/main/data/questions.json`;
}
function updateMetrics() {
  const n = questions.filter(q => reviewed[q.id]).length;
  const pct = questions.length ? Math.round(100 * n / questions.length) : 0;
  $('total').textContent = questions.length;
  $('reviewed').textContent = n;
  $('percent').textContent = `${pct}%`;
  $('areas').textContent = new Set(questions.map(q => q.category)).size;
  $('progressFill').style.width = `${pct}%`;
  $('progress').setAttribute('aria-valuenow', String(pct));
}
function render() {
  const search = $('search').value.toLocaleLowerCase().trim();
  const category = $('category').value, priority = $('priority').value, status = $('status').value;
  const visible = questions.filter(q =>
    (!search || `${q.category} ${q.question} ${q.answer}`.toLocaleLowerCase().includes(search)) &&
    (!category || q.category === category) && (!priority || q.priority === priority) &&
    (!status || (status === 'done' ? !!reviewed[q.id] : !reviewed[q.id]))
  );
  $('count').textContent = `Showing ${visible.length} of ${questions.length} questions`;
  const root = $('questions'); root.replaceChildren();
  const groups = new Map();
  visible.forEach(q => { if (!groups.has(q.category)) groups.set(q.category, []); groups.get(q.category).push(q); });
  for (const [categoryName, list] of groups) {
    const heading = document.createElement('h2'); heading.className = 'group';
    heading.textContent = `${categoryName} (${list.length})`; root.append(heading);
    for (const q of list) {
      const detail = document.createElement('details');
      const summary = document.createElement('summary');
      const check = document.createElement('input'); check.type = 'checkbox'; check.className = 'check';
      check.checked = !!reviewed[q.id]; check.setAttribute('aria-label', `Mark reviewed: ${q.question}`);
      check.addEventListener('click', event => event.stopPropagation());
      check.addEventListener('change', () => { reviewed[q.id] = check.checked; save(); updateMetrics(); if ($('status').value) render(); });
      const number = document.createElement('span'); number.className = 'num'; number.textContent = `#${q.id}`;
      const question = document.createElement('span'); question.className = 'question'; question.textContent = q.question;
      const pill = document.createElement('span'); pill.className = 'pill' + (q.priority === 'Medium' ? ' medium' : ''); pill.textContent = q.priority;
      summary.append(check, number, question, pill);
      const answer = document.createElement('div'); answer.className = 'answer'; answer.textContent = q.answer;
      detail.append(summary, answer); root.append(detail);
    }
  }
  updateMetrics();
}
async function start() {
  configureLinks();
  try {
    const response = await fetch('data/questions.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data)) throw new Error('Expected an array of questions');
    questions = data;
    [...new Set(data.map(q => q.category))].sort().forEach(category => {
      const option = document.createElement('option'); option.value = category; option.textContent = category; $('category').append(option);
    });
    render();
  } catch (error) {
    $('message').textContent = 'Unable to load questions.json. Publish through GitHub Pages or run a local HTTP server (python -m http.server 8000). Details: ' + error.message;
  }
}
['search', 'category', 'priority', 'status'].forEach(id => $(id).addEventListener(id === 'search' ? 'input' : 'change', render));
$('expand').addEventListener('click', () => document.querySelectorAll('details').forEach(el => { el.open = true; }));
$('collapse').addEventListener('click', () => document.querySelectorAll('details').forEach(el => { el.open = false; }));
$('reset').addEventListener('click', () => { if (confirm('Clear your personal revision checkmarks?')) { reviewed = {}; save(); render(); } });
$('export').addEventListener('click', () => {
  const lines = ['ID,Category,Question,Reviewed', ...questions.map(q => [q.id, q.category, q.question, !!reviewed[q.id]].map(safeCsv).join(','))];
  const url = URL.createObjectURL(new Blob([lines.join('\r\n')], { type: 'text/csv;charset=utf-8' }));
  const link = document.createElement('a'); link.href = url; link.download = 'interview-progress.csv'; link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
start();
