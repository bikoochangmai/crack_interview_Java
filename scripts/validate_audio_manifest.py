import json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
m=json.loads((root/'audio/manifest.json').read_text(encoding='utf-8-sig'))
for q,parts in m.items():
 for kind,p in parts.items():
  assert kind in ('question','explanation'), (q,kind)
  f=root/p
  assert f.is_file() and f.stat().st_size>0, f
print(f'Audio manifest valid: {len(m)} questions, {sum(len(v) for v in m.values())} recordings')
