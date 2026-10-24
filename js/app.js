"use strict";
const $ = id => document.getElementById(id);
const OLD_KEY = 'java-interview-prep-reviewed-v2';
const KEY = 'crack-interview-java-progress-v3';
let questions=[], leetcode=[], completed={}, studied={}, activeCategory='';
const STUDY_KEY='crack-interview-java-studied-v1';
try { studied=JSON.parse(localStorage.getItem(STUDY_KEY)||'{}'); if(!studied || typeof studied!=='object' || Array.isArray(studied)) studied={}; } catch { studied={}; }
const saveStudied=()=>{try{localStorage.setItem(STUDY_KEY,JSON.stringify(studied));}catch{}};
try { completed=JSON.parse(localStorage.getItem(KEY) || localStorage.getItem(OLD_KEY) || '{}'); if(!completed || Array.isArray(completed) || typeof completed!=='object') completed={}; } catch { completed={}; }
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(completed));}catch{}};
const all=()=>[...questions.map(q=>({...q,kind:'interview',key:'q:'+q.id})),...leetcode.map(p=>({...p,category:'LeetCode / '+p.topic,priority:p.difficulty,question:p.title,answer:p.approach,kind:'leetcode',key:'lc:'+p.id}))];
const categories=()=>[...new Set(all().map(x=>x.category))];
const done=x=>!!completed[x.key];
function linkRepo(){let host=location.hostname;if(!host.endsWith('.github.io'))return;let owner=host.slice(0,-10),repo=location.pathname.split('/').filter(Boolean)[0]||owner+'.github.io';let root='https://github.com/'+encodeURIComponent(owner)+'/'+encodeURIComponent(repo);$('repo').href=root;$('contribute').href=root+'/blob/main/CONTRIBUTING.md';}
window.interviewAudioItems=all;
function metrics(){let data=all(),n=data.filter(done).length,p=data.length?Math.round(100*n/data.length):0;$('total').textContent=data.length;$('reviewed').textContent=n;$('percent').textContent=p+'%';$('areas').textContent=categories().length;$('progressFill').style.width=p+'%';$('progress').setAttribute('aria-valuenow',p);}
function sectionData(){let result=new Map();for(const x of all()){if(!result.has(x.category))result.set(x.category,[]);result.get(x.category).push(x);}return result;}
function navigation(){let nav=$('navTree');nav.replaceChildren();let allBtn=document.createElement('button');allBtn.type='button';allBtn.className='nav-all'+(!activeCategory?' selected':'');allBtn.textContent='All topics';allBtn.onclick=()=>choose('');nav.append(allBtn);
 let sections=sectionData();let groups=new Map();for(const [name,items] of sections){let group=name.startsWith('Mock Interview')?'Mock Interviews':name.startsWith('Low-Level Design')?'Low-Level Design (LLD)':name.startsWith('High-Level Design')?'High-Level Design (HLD)':name.startsWith('Terraform')||name.startsWith('GitHub Actions')?'DevOps & Infrastructure':name.startsWith('AI Engineering')?'AI Engineering':name.startsWith('System Design')?'High-Level Design (HLD)':name.startsWith('Microservices')?'Microservices':name.startsWith('Design Patterns')?'Design Patterns':name.startsWith('Azure')?'Azure Cloud':name.startsWith('Kafka')?'Apache Kafka':name.startsWith('LeetCode')?'LeetCode / DSA':name.startsWith('Java')||name.startsWith('Core Java')||name.startsWith('Concurrency')?'Java & JVM':name.startsWith('Spring')||name.startsWith('REST')?'Backend & Services':name.startsWith('SQL')?'Databases':name.startsWith('Angular')?'Frontend': 'Architecture & Leadership';if(!groups.has(group))groups.set(group,[]);groups.get(group).push([name,items]);}
 for(const [group,entries] of groups){let details=document.createElement('details');details.className='tree-group';details.open=true;let summary=document.createElement('summary');summary.textContent=group;details.append(summary);if(group==='Mock Interviews'||group.includes('Level Design')||group==='AI Engineering'){let guide=document.createElement('a');guide.href=group==='AI Engineering'?'docs/generative-ai/index.html':group==='Mock Interviews'?'docs/mock/README.md':'docs/lld-hld-learning-path.md';guide.textContent=group==='AI Engineering'?'Generative AI — 20 illustrated sections':group==='Mock Interviews'?'Practice guide and all model answers':'LLD / HLD learning paths';guide.className='tree-guide';details.append(guide);}
 for(const [name,items] of entries){let line=document.createElement('div');line.className='tree-line'+(activeCategory===name?' selected':'');let check=document.createElement('input');check.type='checkbox';check.className='tree-check';check.checked=items.every(done);check.indeterminate=!check.checked&&items.some(done);check.title='Mark all items in '+name+' complete';check.setAttribute('aria-label','Complete section '+name);check.onchange=()=>{items.forEach(x=>completed[x.key]=check.checked);save();refresh();};let btn=document.createElement('button');btn.type='button';btn.className='tree-link';btn.textContent=name;btn.title=name;btn.onclick=()=>choose(name);let count=document.createElement('span');count.className='tree-count';count.textContent=items.filter(done).length+'/'+items.length;if(check.checked)count.textContent='✓ '+count.textContent;line.append(check,btn,count);details.append(line);}nav.append(details);}
}
function choose(category){activeCategory=category;$('category').value=category;refresh();}
function addText(parent,tag,content,cls){let el=document.createElement(tag);if(cls)el.className=cls;el.textContent=content;parent.append(el);return el;}
// Self-contained, keyboard-accessible walkthroughs; no external diagram service.
function renderDesignLesson(parent, item) {
 if (!Array.isArray(item.walkthroughSteps) || !item.walkthroughSteps.length) return;
 addText(parent,'h3','Visual walkthrough — '+item.learningTitle);
 const figure=document.createElement('figure');figure.className='design-figure';
 const link=document.createElement('a');link.href=item.diagramImage;link.target='_blank';link.rel='noopener';
 const img=document.createElement('img');img.src=item.diagramImage;img.alt=item.learningTitle+': '+item.diagram;img.loading='lazy';img.width=960;img.height=960;
 link.append(img);figure.append(link);addText(figure,'figcaption','Illustrative flow. Select the image to open it at full size; use the steps below to follow the example.');parent.append(figure);
 const panel=document.createElement('section');panel.className='design-walkthrough';panel.setAttribute('aria-label','Step-by-step request walkthrough');
 const controls=document.createElement('div');controls.className='design-step-buttons';
 const detail=document.createElement('div');detail.setAttribute('aria-live','polite');detail.setAttribute('aria-atomic','true');
 const buttons=[];
 const show=index=>{detail.replaceChildren();buttons.forEach((b,i)=>{b.setAttribute('aria-pressed',String(i===index));});const step=item.walkthroughSteps[index];addText(detail,'h4','Step '+(index+1)+' of '+item.walkthroughSteps.length+' — '+step.title);addText(detail,'p',step.explanation);};
 item.walkthroughSteps.forEach((step,i)=>{const b=document.createElement('button');b.type='button';b.textContent=(i+1)+'. '+step.title;b.onclick=()=>show(i);buttons.push(b);controls.append(b);});
 panel.append(controls,detail);parent.append(panel);show(0);
 addText(parent,'h3','Check your understanding');addText(parent,'p',item.knowledgeCheck);
 const guide=document.createElement('a');guide.href=item.guidePath||'docs/system-design/visual-learning-guide.md';guide.textContent='Beginner glossary and complete visual study guide';parent.append(guide);
}

function render(){let search=$('search').value.trim().toLowerCase(),cat=$('category').value,priority=$('priority').value,status=$('status').value;
 let data=all(),visible=data.filter(x=>(!cat||x.category===cat)&&(!priority||x.priority===priority)&&(!status||(status==='done'?done(x):!done(x)))&&(!search||[x.category,x.question,x.answer,x.example||'',x.problem||'',x.code||'',x.constraints||'',x.bruteForce||'',x.walkthrough||'',x.explanation||'',x.learningTitle||'',x.knowledgeCheck||'',...(x.lessonSections||[]).map(section=>section.title+' '+section.explanation),...(x.walkthroughSteps||[]).map(step=>step.title+' '+step.explanation),...(x.contentBlocks||[]).map(b=>b.text)].join(' ').toLowerCase().includes(search)));
 $('count').textContent='Showing '+visible.length+' of '+data.length+' items';let root=$('questions');root.replaceChildren();if(!visible.length)addText(root,'p','No matching questions. Try clearing filters.','empty');let groups=new Map();for(const x of visible){if(!groups.has(x.category))groups.set(x.category,[]);groups.get(x.category).push(x);}
 for(const [name,items] of groups){addText(root,'h2',name+' ('+items.length+')','group');for(const x of items){let details=document.createElement('details'),summary=document.createElement('summary'),check=document.createElement('input');check.type='checkbox';check.className='check';check.checked=done(x);check.setAttribute('aria-label','Mark complete: '+x.question);check.onclick=e=>e.stopPropagation();check.onchange=()=>{completed[x.key]=check.checked;save();refresh();};addText(summary,'span',x.kind==='leetcode'?x.id:'#'+x.id,'num');summary.prepend(check);addText(summary,'span',x.question,'question');addText(summary,'span',x.priority,'pill'+(x.priority==='Medium'?' medium':'')+(x.priority==='Easy'?' easy':''));details.append(summary);
 let body=document.createElement('div');body.className='answer';if(x.kind==='leetcode'){addText(body,'h3','Problem');addText(body,'p',x.problem);addText(body,'h3','Input, output and constraints');addText(body,'p',x.constraints);addText(body,'h3','Worked example');addText(body,'p',x.example,'example');addText(body,'h3','Brute-force baseline');addText(body,'p',x.bruteForce);addText(body,'p','Time: '+x.bruteTime+' · Space: '+x.bruteSpace,'complexity');let brutePre=document.createElement('pre');addText(brutePre,'code',x.bruteCode);body.append(brutePre);addText(body,'h3','Why this approach works');addText(body,'p',x.approach);addText(body,'h3','Step-by-step explanation');addText(body,'p',x.walkthrough);addText(body,'h3','Edge cases');addText(body,'p',x.edgeCases);addText(body,'h3','Interview walkthrough');addText(body,'p','Start with the brute-force idea, identify its bottleneck, then explain how the chosen data structure or algorithm improves it. Walk through the example input and discuss empty inputs, duplicates and boundary conditions.');addText(body,'p','Time: '+x.time+' · Space: '+x.space,'complexity');addText(body,'h3','Java solution');let pre=document.createElement('pre');let code=document.createElement('code');code.textContent=x.code;pre.append(code);body.append(pre);}else if(Array.isArray(x.contentBlocks)){
  for(const block of x.contentBlocks){
   if(block.type==='chapter'){addText(body,'h2',block.text,'ai-topic-heading');}
   else if(block.type==='heading'){addText(body,'h3',block.text);}
   else if(block.type==='references'){const refs=document.createElement('p');refs.className='ai-references';refs.append(document.createTextNode('Further reading: '));block.links.forEach((source,i)=>{if(!/^https:\/\//.test(source.url))return;if(i)refs.append(document.createTextNode(' · '));const link=addText(refs,'a',source.label);link.href=source.url;link.target='_blank';link.rel='noopener';});body.append(refs);}
   else if(block.type==='list'||block.type==='checklist'){const list=document.createElement('ul');for(const item of block.items)addText(list,'li',item);body.append(list);}
   else if(block.type==='table'){const wrap=document.createElement('div');wrap.className='ai-table-scroll';wrap.tabIndex=0;wrap.setAttribute('role','region');wrap.setAttribute('aria-label','Scrollable study table');const table=document.createElement('table'),head=document.createElement('thead'),row=document.createElement('tr');for(const title of block.headers){const th=addText(row,'th',title);th.scope='col';}head.append(row);table.append(head);const rows=document.createElement('tbody');for(const values of block.rows){const tr=document.createElement('tr');values.forEach((value,i)=>{const cell=addText(tr,i===0?'th':'td',value);if(i===0)cell.scope='row';});rows.append(tr);}table.append(rows);wrap.append(table);body.append(wrap);}
   else if(block.type==='note'){addText(body,'aside',block.text,'ai-clarification');}
   else if(block.type==='image'&&typeof block.path==='string'&&/^docs\/[a-zA-Z0-9_./-]+\.svg$/.test(block.path)&&!block.path.includes('..')){const figure=document.createElement('figure');figure.className='tutorial-figure';if(Array.isArray(block.layers)){figure.classList.add('ai-diagram');const mobile=document.createElement('div');mobile.className='ai-mobile-flow';addText(mobile,'h4',block.text);block.layers.forEach((layer,r)=>{if(r)addText(mobile,'div','↓','ai-flow-arrow');const stage=document.createElement('div');layer.forEach((label,c)=>addText(stage,'div',label,'ai-flow-card ai-tone-'+((r+c)%6)));mobile.append(stage);});addText(mobile,'p','Grouped cards show parallel paths. Open the full chart to inspect branches and feedback connections.');figure.append(mobile);}const link=document.createElement('a');link.href=block.path;link.target='_blank';link.rel='noopener';const img=document.createElement('img');img.src=block.path;img.alt=block.text;img.loading='lazy';link.append(img);figure.append(link);addText(figure,'figcaption',block.text+' — select to open at full size');body.append(figure);}
   else if(block.type==='code'){let pre=document.createElement('pre');addText(pre,'code',block.text);body.append(pre);}
   else{addText(body,'p',block.text,'tutorial-text');}
  }
 }else{
  const isExpanded=x.detailStatus==='Expanded'||(!x.detailStatus&&!!x.why);
  if(x.detailStatus&&x.detailStatus.includes('code pending'))addText(body,'p','Production scenario provided. A standalone runnable code example is still pending for this question.','note');
  addText(body,'h3','What is it? — Concept');addText(body,'p',x.explanation||x.answer);
  if(x.why){addText(body,'h3','Why and when is it used?');addText(body,'p',x.why);}
  if(x.example){addText(body,'h3','Real-world / production example');addText(body,'p',x.example,'example');}
  if(Array.isArray(x.lessonSections)){for(const section of x.lessonSections){addText(body,'h3',section.title);addText(body,'p',section.explanation);}}
  if(x.diagram){addText(body,'h3','Architecture / execution flow');addText(body,'p',x.diagram,'example');}if(x.runCommand){addText(body,'p','Run locally: '+x.runCommand,'complexity');}if(x.mockBruteCode){addText(body,'h3','Brute-force Java baseline');const pre=document.createElement('pre');addText(pre,'code',x.mockBruteCode);body.append(pre);}
  if(x.code){addText(body,'h3',x.labType ? x.labType+' runnable lab' : 'Java example');if(x.labPath)addText(body,'p','Source file: '+x.labPath,'complexity');let pre=document.createElement('pre');let code=document.createElement('code');code.textContent=x.code;pre.append(code);body.append(pre);}
  if(x.tradeoffs){addText(body,'h3','Trade-offs and failure modes');addText(body,'p',x.tradeoffs);}
  if(Array.isArray(x.followups)&&x.followups.length){addText(body,'h3','Interview follow-up questions');let ul=document.createElement('ul');for(const f of x.followups)addText(ul,'li',f);body.append(ul);}
  if(x.detailStatus==='Guided study — example needs review')addText(body,'p','Study prompt only: verify this scenario and add a runnable code example before treating it as a complete answer.','note');
}
if(x.notesPath){const guide=document.createElement('a');guide.href=x.notesPath;guide.className='notes-guide-link';guide.textContent='Open these notes in a full-width study page';body.prepend(guide);}
if(x.studyGuide){const guide=document.createElement('a');guide.href=x.studyGuide;guide.textContent='Full mock-round guide and solutions';body.append(guide);}
renderDesignLesson(body,x);
if(window.interviewAudio)window.interviewAudio.attach(body,x);
let actions=document.createElement('div');actions.className='study-actions';let read=document.createElement('label');read.className='studied-label';let readCheck=document.createElement('input');readCheck.type='checkbox';readCheck.checked=!!studied[x.key];readCheck.setAttribute('aria-label','Mark studied: '+x.question);readCheck.onchange=()=>{studied[x.key]=readCheck.checked;saveStudied();};read.append(readCheck,document.createTextNode(' Studied / read'));actions.append(read);let master=document.createElement('label');master.className='mastered-label';let masterCheck=document.createElement('input');masterCheck.type='checkbox';masterCheck.checked=done(x);masterCheck.setAttribute('aria-label','Mark mastered: '+x.question);masterCheck.onchange=()=>{completed[x.key]=masterCheck.checked;save();refresh();};master.append(masterCheck,document.createTextNode(' ✓ Mastered (green navigation tick)'));actions.append(master);body.append(actions);
details.append(body);root.append(details);}}
 metrics();}
function refresh(){navigation();render();}
async function start(){linkRepo();try{let results=await Promise.all(['data/questions.json','data/leetcode.json'].map(async url=>{let r=await fetch(url,{cache:'no-cache'});if(!r.ok)throw Error(url+': HTTP '+r.status);return r.json();}));[questions,leetcode]=results;if(!Array.isArray(questions)||!Array.isArray(leetcode))throw Error('Expected JSON arrays');for(const cat of categories()){let opt=document.createElement('option');opt.value=cat;opt.textContent=cat;$('category').append(opt);}refresh();}catch(e){$('message').textContent='Unable to load learning data. Use GitHub Pages or a local HTTP server. '+e.message;}}
['search','priority','status'].forEach(id=>$(id).addEventListener(id==='search'?'input':'change',render));$('category').addEventListener('change',()=>{activeCategory=$('category').value;refresh();});
$('expand').onclick=()=>document.querySelectorAll('#questions details').forEach(x=>x.open=true);$('collapse').onclick=()=>document.querySelectorAll('#questions details').forEach(x=>x.open=false);
$('navToggle').onclick=()=>{let nav=$('navTree'),hidden=nav.hidden;nav.hidden=!hidden;$('navToggle').textContent=hidden?'Collapse':'Expand';$('navToggle').setAttribute('aria-expanded',String(hidden));};
$('reset').onclick=()=>{if(confirm('Clear ALL personal interview and LeetCode completion marks on this browser?')){completed={};studied={};save();saveStudied();refresh();}};
const csv=v=>'"'+String(v).replace(/"/g,'""').replace(/^[=+@\-\t\r]/,"'")+'"';
$('export').onclick=()=>{let rows=['ID,Section,Question,Studied,Mastered',...all().map(x=>[x.key,x.category,x.question,!!studied[x.key],done(x)].map(csv).join(','))];let url=URL.createObjectURL(new Blob([rows.join('\r\n')],{type:'text/csv;charset=utf-8'}));let a=document.createElement('a');a.href=url;a.download='java-interview-progress.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};
start();
// Three navigation modes: hidden (maximum reading width), slide-out, and V5-style docked tree.
// The progress storage keys are unchanged and never touched by these controls.
const NAV_MODE_KEY='crack-interview-java-nav-mode-v63';
const workspace=$('workspace'),sidebar=$('learningSidebar'),sidebarToggle=$('sidebarToggle');
const sidebarBackdrop=$('sidebarBackdrop'),dockToggle=$('dockToggle'),readingToggle=$('readingToggle');
let navMode='docked';
try {
  const saved=localStorage.getItem(NAV_MODE_KEY);
  if(['hidden','drawer','docked'].includes(saved)) navMode=saved;
} catch {}
function setNavMode(mode,focusToggle=false){
  if(!['hidden','drawer','docked'].includes(mode)) return;
  navMode=mode;
  workspace.classList.toggle('drawer-open',mode==='drawer');
  workspace.classList.toggle('nav-docked',mode==='docked');
  workspace.classList.toggle('sidebar-collapsed',mode==='hidden');
  sidebar.removeAttribute('hidden');
  const closed=mode==='hidden';
  sidebar.toggleAttribute('inert',closed);
  sidebar.setAttribute('aria-hidden',String(closed));
  sidebarBackdrop.hidden=mode!=='drawer';
  sidebarToggle.textContent=closed?'☰ Topics':mode==='drawer'?'✕ Close topics':'☰ Hide tree';
  sidebarToggle.setAttribute('aria-label',closed?'Open learning topics':mode==='drawer'?'Close slide-out topics':'Hide docked learning tree');
  sidebarToggle.setAttribute('aria-expanded',String(!closed));
  dockToggle.textContent=mode==='docked'?'↗ Slide-out instead':'▤ Pin tree (V5 view)';
  dockToggle.setAttribute('aria-pressed',String(mode==='docked'));
  readingToggle.textContent=mode==='docked'?'⛶ Full-width reading':'▤ Return to study tree';
  readingToggle.setAttribute('aria-pressed',String(mode==='hidden'));
  readingToggle.setAttribute('aria-label',mode==='docked'?'Switch to full-width reading mode':'Return to pinned study tree');
  try{localStorage.setItem(NAV_MODE_KEY,mode);}catch{}
  if(focusToggle)sidebarToggle.focus();
}
setNavMode(navMode);
sidebarToggle.addEventListener('click',()=>setNavMode(navMode==='hidden'?'drawer':'hidden'));
dockToggle.addEventListener('click',()=>setNavMode(navMode==='docked'?'drawer':'docked'));
readingToggle.addEventListener('click',()=>setNavMode(navMode==='docked'?'hidden':'docked'));
sidebarBackdrop.addEventListener('click',()=>setNavMode('hidden',true));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&navMode==='drawer')setNavMode('hidden',true);});
