"""Check published tutorial coverage, local links and portal/source consistency."""
import json,re,sys
from pathlib import Path
from xml.etree import ElementTree
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from system_design_tutorials import JOURNEYS,FOUNDATIONS,content_blocks

def main():
 questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
 lessons=[q for q in questions if q['category'].startswith('System Design')]
 assert {q['id'] for q in lessons}==set(range(233,259))
 assert len(JOURNEYS)==9 and len(FOUNDATIONS)==10
 docs=[ROOT/'docs/system-design'/f'{slug}.md' for slug in ['short-url',*JOURNEYS]]
 for doc in docs:
  source=doc.read_text(encoding='utf-8-sig')
  assert len(re.findall(r'^## ',source,re.M))>=8,doc
  for phrase in ('auth','fail','domain'):
   assert phrase in source.lower(),(doc,phrase)
  assert 'Describe core user journeys' not in source,doc
  for match in re.finditer(r'\]\(([^)]+)\)',source):
   target=match[1]
   if target.startswith(('http:','https:','#','mailto:')):continue
   assert (doc.parent/target.split('#')[0]).resolve().is_file(),(doc,target)
 for q in lessons:
  assert len(q['walkthroughSteps'])==4
  assert (ROOT/q['guidePath']).is_file()
  assert (ROOT/q['diagramImage']).is_file()
  if q['id']<243:assert len(q['lessonSections'])==2
  for b in q.get('contentBlocks',[]):
   assert b.get('type') in ('heading','text','code','image')
   assert isinstance(b.get('text'),str) and b['text']
   if b['type']=='image':assert (ROOT/b['path']).is_file()
 for ident in (243,246,250,255):
  q=next(q for q in lessons if q['id']==ident)
  assert q['contentBlocks']==content_blocks((ROOT/q['guidePath']).read_text(encoding='utf-8-sig'))
 short=(ROOT/'docs/system-design/short-url.md').read_text(encoding='utf-8')
 for phrase in ('302 Found','Location:','PUBLIC_SHORT_ORIGIN','CNAME','RESTRICTED','503','404','401','403','ON CONFLICT','Idempotency-Key'):
  assert phrase in short,phrase
 for file in (ROOT/'docs/system-design/diagrams').glob('*.svg'):
  svg=ElementTree.parse(file).getroot();assert svg.tag.endswith('svg')
 print('Validated ten case tutorials, ten foundations, all 26 portal lessons, diagram XML and local links.')

if __name__=='__main__':main()
