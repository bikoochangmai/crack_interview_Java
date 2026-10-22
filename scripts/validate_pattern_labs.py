"""Compile/run eight standard-library Java 21 labs and verify embedded code stays in sync."""
from pathlib import Path
import json,subprocess,tempfile
ROOT=Path(__file__).resolve().parents[1]
def main():
 questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
 lessons=[q for q in questions if q['category'].startswith('Design Patterns')]
 assert {q['id'] for q in lessons}==set(range(266,274))
 for q in lessons:
  assert len(q['walkthroughSteps'])==4 and len(q['lessonSections'])>=5
  assert (ROOT/q['labPath']).read_text(encoding='utf-8')==q['code']
  assert (ROOT/q['diagramImage']).is_file() and (ROOT/q['guidePath']).is_file()
 with tempfile.TemporaryDirectory(prefix='pattern-lab-check-',dir=ROOT) as target:
  target=Path(target);assert target.resolve().parent==ROOT.resolve()
  subprocess.run(['javac','-encoding','UTF-8','--release','21','-d',str(target),*[str(ROOT/q['labPath']) for q in lessons]],check=True)
  for q in lessons:
   result=subprocess.run(['java','-cp',str(target),'Pattern'+str(q['id'])],check=True,capture_output=True,text=True,timeout=15)
   assert result.stdout.startswith('PASS:'),result.stdout
   print(q['id'],result.stdout.strip())
 print('Passed eight Java pattern labs, negative cases, diagram paths and content synchronization.')
if __name__=='__main__':main()
