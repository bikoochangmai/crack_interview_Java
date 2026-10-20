#!/usr/bin/env python3
import json,sys
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'leetcode.json'
try: data=json.loads(p.read_text(encoding='utf-8'))
except (OSError,ValueError) as e:sys.exit(str(e))
if not isinstance(data,list) or not data:sys.exit('leetcode.json must be a nonempty array')
ids=set()
for i,x in enumerate(data,1):
    for field in ('id','title','difficulty','topic','problem','example','approach','time','space','language','code'):
        if not isinstance(x.get(field),str) or not x[field].strip():sys.exit(f'Entry {i}: invalid {field}')
    if x['id'] in ids:sys.exit(f'Duplicate ID: {x["id"]}')
    ids.add(x['id'])
    if x['difficulty'] not in ('Easy','Medium','Hard'):sys.exit(f'Entry {i}: invalid difficulty')
print(f'Validated {len(data)} Java coding problems.')
