#!/usr/bin/env python3
"""Generate full-length neural-voice MP3 audio for GitHub Pages.
Requires: py -m pip install edge-tts ; FFmpeg only for long passages.
Uses Microsoft's online Edge TTS service via an unofficial client; availability and
terms may change. Content is sent to the TTS service. No API key required currently.
"""
import argparse, asyncio, json, re, shutil, subprocess, tempfile
from pathlib import Path
import edge_tts

ROOT = Path(__file__).resolve().parents[1]

def full_text(q):
    chunks=[q.get('question'),q.get('answer'),q.get('explanation'),q.get('why'),q.get('example'),q.get('tradeoffs')]
    chunks += q.get('followups',[]) if isinstance(q.get('followups'),list) else []
    chunks=[str(x).strip() for x in chunks if x]
    return '. '.join(chunks)

def split_text(text, maxlen=2300):
    sentences=re.split(r'(?<=[.!?])\s+',text)
    parts=[];current=''
    for sentence in sentences:
        while len(sentence)>maxlen:
            if current:parts.append(current);current=''
            cut=sentence.rfind(' ',0,maxlen)
            if cut<maxlen//2:cut=maxlen
            parts.append(sentence[:cut].strip());sentence=sentence[cut:].strip()
        if len(current)+len(sentence)+1>maxlen and current:
            parts.append(current);current=''
        current=(current+' '+sentence).strip()
    if current:parts.append(current)
    return parts

async def generate(q,voice,rate,force):
    qid=str(q['id']); text=full_text(q)
    if not text:return None
    dest=ROOT/'audio'/'full'/f'{qid}.mp3';dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and not force:return 'audio/full/'+qid+'.mp3'
    parts=split_text(text)
    with tempfile.TemporaryDirectory() as td:
        paths=[]
        for i,part in enumerate(parts):
            path=Path(td)/f'{i:04}.mp3'
            await edge_tts.Communicate(part,voice,rate=rate).save(str(path))
            if not path.exists() or path.stat().st_size==0:raise RuntimeError('Empty speech output')
            paths.append(path)
        if len(paths)==1:shutil.copyfile(paths[0],dest)
        else:
            if not shutil.which('ffmpeg'):
                raise RuntimeError('FFmpeg required for long answers; install FFmpeg and retry')
            listing=Path(td)/'list.txt'
            listing.write_text(''.join(f"file '{str(path).replace(chr(39), chr(39)+chr(92)+chr(39)+chr(39))}'\n" for path in paths),encoding='utf-8')
            subprocess.run(['ffmpeg','-nostdin','-v','error','-y','-f','concat','-safe','0','-i',str(listing),'-c','copy',str(dest)],check=True)
    return 'audio/full/'+qid+'.mp3'

async def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--scope',choices=['sample','all'],default='sample')
    parser.add_argument('--voice',default='en-US-AriaNeural')
    parser.add_argument('--rate',default='+0%')
    parser.add_argument('--force',action='store_true',help='Regenerate existing full recordings')
    args=parser.parse_args()
    questions=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
    selected=questions[:3] if args.scope=='sample' else questions
    manifest_path=ROOT/'audio/manifest.json'
    manifest=json.loads(manifest_path.read_text(encoding='utf-8-sig')) if manifest_path.exists() else {}
    failures=[]
    for i,q in enumerate(selected,1):
        try:
            path=await generate(q,args.voice,args.rate,args.force)
            if path:
                manifest.setdefault(str(q['id']),{})['full']=path
                manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
                print(f"[{i}/{len(selected)}] Generated question {q['id']}: {path}",flush=True)
        except Exception as exc:
            print(f"FAILED question {q['id']}: {exc}",flush=True)
            failures.append(q['id'])
    if failures:raise SystemExit(f'Failed IDs: {failures}')

if __name__=='__main__':asyncio.run(main())
