from pathlib import Path
import json, re, subprocess, sys
root=Path(__file__).resolve().parent.parent
qs=json.loads((root/'data/questions.json').read_text())
labs=[q for q in qs if q.get('labPath','').startswith('examples/v6/')]
assert len(labs)==103,len(labs)
assert len({q['id'] for q in labs})==103
assert all((root/q['labPath']).is_file() for q in labs)
assert len([q for q in labs if q['labType']=='Java 21'])==73
assert len([q for q in labs if q['labType']=='PostgreSQL'])==16
assert len([q for q in labs if q['labType']=='TypeScript'])==14
assert not any(q.get('detailStatus','').endswith('code pending') for q in qs)
print('V6 manifest validated: 103 labs (73 Java 21 / 16 SQL / 14 TypeScript).')
