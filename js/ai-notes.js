"use strict";
(() => {
 const sections=[...document.querySelectorAll('.note-section')];
 const entries=[...document.querySelectorAll('.contents li')];
 const input=document.getElementById('notes-search');
 const status=document.getElementById('notes-status');
 const key='generative-ai-illustrated-notes-v1';
 let progress={};
 try{const saved=JSON.parse(localStorage.getItem(key)||'{}');if(saved&&typeof saved==='object'&&!Array.isArray(saved))progress=saved;}catch{}
 const normalize=text=>text.normalize('NFKC').toLowerCase().replace(/\s+/g,' ').trim();
 const searchText=sections.map(section=>normalize(section.textContent+' '+[...section.querySelectorAll('img')].map(img=>img.alt).join(' ')));
 function update(){
  const query=normalize(input.value),terms=query.split(' ').filter(Boolean);
  let shown=0;
  sections.forEach((section,i)=>{const match=terms.every(term=>searchText[i].includes(term));section.hidden=!match;entries[i].hidden=!match;if(match)shown++;});
  const completed=sections.filter((_,i)=>progress['page-'+(i+1)]===true).length;
  status.textContent=shown+' of 20 sections shown · '+completed+' sections studied · Progress is stored in this browser.';
 }
 document.querySelectorAll('[data-check]').forEach(check=>{
  check.checked=progress[check.dataset.check]===true;
  check.addEventListener('change',()=>{progress[check.dataset.check]=check.checked;try{localStorage.setItem(key,JSON.stringify(progress));}catch{}update();});
 });
 input.addEventListener('input',update);
 document.getElementById('show-all').addEventListener('click',()=>{input.value='';update();input.focus();});
 document.getElementById('print-notes').addEventListener('click',()=>window.print());
 // Previous/next and direct hash links also work after a search hides sections.
 function revealHash(){const target=document.getElementById(location.hash.slice(1));if(target&&target.hidden){input.value='';update();target.scrollIntoView();}}
 window.addEventListener('hashchange',revealHash);
 update();revealHash();
})();
