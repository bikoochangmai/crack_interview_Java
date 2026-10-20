#!/usr/bin/env python3
"""Validate content changes proposed via GitHub pull requests."""
import json
import sys
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'data' / 'questions.json'
try:
    questions = json.loads(path.read_text(encoding='utf-8'))
except (ValueError, OSError) as exc:
    sys.exit(f'Invalid JSON: {exc}')
if not isinstance(questions, list) or not questions:
    sys.exit('questions.json must be a non-empty JSON array')
ids = set()
errors = []
for i, q in enumerate(questions, 1):
    if not isinstance(q, dict):
        errors.append(f'Entry {i} must be an object')
        continue
    if not isinstance(q.get('id'), int) or isinstance(q.get('id'), bool) or q['id'] < 1:
        errors.append(f'Entry {i}: id must be a positive integer')
    elif q['id'] in ids:
        errors.append(f'Entry {i}: duplicate id {q["id"]}')
    else:
        ids.add(q['id'])
    for field in ('category', 'question', 'answer'):
        if not isinstance(q.get(field), str) or not q[field].strip():
            errors.append(f'Entry {i}: {field} must be a non-empty string')
    if q.get('priority') not in ('High', 'Medium'):
        errors.append(f'Entry {i}: priority must be High or Medium')
if errors:
    sys.exit('\n'.join(errors))
print(f'Validated {len(questions)} questions across {len({q["category"] for q in questions})} categories.')
