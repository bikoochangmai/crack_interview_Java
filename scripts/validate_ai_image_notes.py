"""Validate the image-to-HTML transcription, local links and SVG assets offline."""
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree
import json
import re

ROOT=Path(__file__).resolve().parents[1]
GUIDE=ROOT/'docs/generative-ai/index.html'

class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.text=[]; self.ids=[]; self.links=[]; self.tables=0
    def handle_data(self, data): self.text.append(data)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='table':self.tables+=1
        for key in ('href','src'):
            if attrs.get(key):self.links.append(attrs[key])

def normal(text): return re.sub(r'\s+',' ',text).strip()

def main():
    pages=json.loads((ROOT/'data/ai-study-notes.json').read_text(encoding='utf-8'))
    assert [p['page'] for p in pages]==list(range(1,21))
    assert len({p['sourceFile'] for p in pages})==20
    expected=[0,6,8,7,8,8,8,8,8,10,8,8,8,8,10,9,9,9,10,10]
    assert [sum(b['type']=='heading' for b in p['blocks']) for p in pages]==expected
    text=GUIDE.read_text(encoding='utf-8'); doc=Document();doc.feed(text)
    assert len(doc.ids)==len(set(doc.ids)), 'Duplicate HTML IDs'
    assert all(f'page-{i:02}' in doc.ids for i in range(1,21))
    rendered=normal(' '.join(doc.text)); diagrams=[]; tables=0
    for page in pages:
        assert page['title'] in rendered
        for b in page['blocks']:
            if b['type'] in ('heading','paragraph','note','code'):assert normal(b['text']) in rendered,(page['page'],b)
            elif b['type'] in ('list','checklist'):
                for item in b['items']:assert normal(item) in rendered
            elif b['type']=='table':
                tables+=1
                for row in b['rows']:
                    assert len(row)==len(b['headers']),(page['page'],row)
                    for cell in row:assert normal(cell) in rendered
            elif b['type'] in ('diagram','scatter'):
                file=ROOT/b['path']; diagrams.append(file)
                svg=ElementTree.parse(file).getroot();assert svg.tag.endswith('svg')
                assert svg.get('role')=='img' and svg.get('aria-labelledby')
                assert '<script' not in file.read_text(encoding='utf-8')
    assert len(diagrams)==39 and len(set(diagrams))==39
    assert doc.tables==tables
    assert len([b for b in pages[-1]['blocks'] if b['type']=='table'])==8
    assert sum(len(b['rows']) for b in pages[-1]['blocks'] if b['type']=='table')==40
    for link in doc.links:
        if link.startswith('#'):assert link[1:] in doc.ids,link
        else:
            assert not link.startswith(('http:','https:')), 'Study page must be self-contained'
            assert (GUIDE.parent/link).resolve().is_file(),link
    published=[GUIDE,ROOT/'data/ai-study-notes.json',*diagrams]
    for path in published:
        assert 'rahul yadav' not in path.read_text(encoding='utf-8').lower(),path
        assert '.jpeg' not in path.read_text(encoding='utf-8').lower() or path.suffix=='.json',path
    questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
    item=next(q for q in questions if q['id']==406)
    assert item['notesPath']=='docs/generative-ai/index.html'
    assert item['category'].startswith('AI Engineering') and 'lessonSections' not in item
    assert len([b for b in item['contentBlocks'] if b['type']=='chapter'])==20
    assert len([b for b in item['contentBlocks'] if b['type']=='table'])==tables
    assert len([b for b in item['contentBlocks'] if b['type']=='image'])==39
    assert 'source page' not in text.lower()
    assert 'Open the single-page illustrated guide and select this subsection' not in json.dumps(item)
    print(f'PASS: one HTML page, 20 source pages, {tables} complete tables, 39 SVG diagrams, 40 interview prompts, all local links, no removed name or embedded source photos.')

if __name__=='__main__':main()
