"""Check new study-path/mock coverage and run all eight new Java 21 labs."""
from pathlib import Path
from collections import Counter
from xml.etree import ElementTree
import json,re,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]
LABS=['ParkingLotDemo','TicTacToeDemo','LruCacheDemo','StripedMapDemo','TokenBucketDemo','MockCodingDemo','AtmDemo','OrderBookDemo']
def main():
 questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
 lld=[q for q in questions if q['category']=='Low-Level Design — LLD']
 assert {q['id'] for q in lld}==set(range(367,372))
 for q in lld:
  assert len(q['walkthroughSteps'])==4 and len(q['lessonSections'])>=5
  assert q['code']==(ROOT/q['labPath']).read_text(encoding='utf-8')
  assert (ROOT/q['guidePath']).is_file()
  ElementTree.parse(ROOT/q['diagramImage'])
 for ident in (372,373):
  q=next(q for q in questions if q['id']==ident);assert q['category'].startswith('High-Level Design') and q['contentBlocks']
 mock=[q for q in questions if q['category'].startswith('Mock Interview')]
 assert {q['id'] for q in mock}==set(range(374,406))
 assert Counter(q['category'].split(' — ',1)[1] for q in mock)=={'DSA / Coding':8,'Low-Level Design':4,'System Design':4,'Java / Spring':3,'AI Rounds':10,'Behavioral':3}
 for q in mock:
  assert q['lessonSections'] and q['followups'] and q['example'];assert (ROOT/q['studyGuide']).is_file()
 for path in [ROOT/'docs/lld-hld-learning-path.md',*list((ROOT/'docs/lld').glob('*.md')),*list((ROOT/'docs/mock').glob('*.md')),ROOT/'docs/system-design/distributed-key-value-store.md']:
  text=path.read_text(encoding='utf-8-sig')
  for match in re.finditer(r'\]\(([^)]+)\)',text):
   dest=match[1]
   if dest.startswith(('http:','https:','#')):continue
   assert (path.parent/dest.split('#')[0]).resolve().is_file(),(path,dest)
 with tempfile.TemporaryDirectory(prefix='learning-lab-check-',dir=ROOT) as output:
  output=Path(output);assert output.resolve().parent==ROOT.resolve()
  sources=[next((ROOT/'examples').rglob(name+'.java')) for name in LABS]
  subprocess.run(['javac','-encoding','UTF-8','--release','21','-d',str(output),*[str(p) for p in sources]],check=True)
  for name in LABS:
   result=subprocess.run(['java','-cp',str(output),name],check=True,capture_output=True,text=True,timeout=20)
   assert result.stdout.startswith('PASS:'),(name,result.stdout);print(name+': '+result.stdout.strip())
 print('Validated five LLD lessons, two HLD entries, 32 mock answers, local links and eight Java labs.')
if __name__=='__main__':main()
