"use strict";
// V6.6: real HTMLAudioElement playback for mobile media sessions, optional Web Speech fallback.
(() => {
  const PREF='crack-interview-java-mobile-audio-v66';
  let prefs={rate:1,autoNext:false};
  try{prefs={...prefs,...JSON.parse(localStorage.getItem(PREF)||'{}')};}catch{}
  const save=()=>{try{localStorage.setItem(PREF,JSON.stringify(prefs));}catch{}};
  const audio=new Audio(); audio.preload='none'; audio.playsInline=true;
  let manifest={}, queue=[], index=-1, current=null, fallback=null, token=0;
  const status=()=>document.getElementById('mobileAudioStatus');
  const player=()=>document.getElementById('mobileAudioPlayer');
  const setStatus=s=>{if(status())status().textContent=s;};
  const setTitle=s=>{const el=document.getElementById('mobileAudioTitle');if(el)el.textContent=s;};
  const setPlaying=()=>{const el=document.getElementById('mobileAudioPlay');if(el)el.textContent=audio.paused?'▶ Play':'⏸ Pause';};
  const supportsSpeech=!!(window.speechSynthesis&&window.SpeechSynthesisUtterance);
  const stopSpeech=()=>{token++;if(supportsSpeech)window.speechSynthesis.cancel();fallback=null;};
  const idOf=x=>String(x.id);
  const pathFor=(x,kind)=>x.kind==='leetcode'?null:manifest[idOf(x)]?.[kind]||null;
  function updateMediaSession(x){
    if(!('mediaSession' in navigator))return;
    try{
      navigator.mediaSession.metadata=new MediaMetadata({title:x.question||x.title||'Interview question',artist:'Java Interview Prep Hub',album:'Interview study audio'});
      for(const [action,fn] of [['play',()=>audio.play()],['pause',()=>audio.pause()],['nexttrack',()=>step(1)],['previoustrack',()=>step(-1)]]){
        try{navigator.mediaSession.setActionHandler(action,fn);}catch{}
      }
    }catch{}
  }
  function stop(){stopSpeech();audio.pause();audio.removeAttribute('src');audio.load();current=null;setStatus('Stopped');setPlaying();}
  function speakFallback(x,kind){
    if(!supportsSpeech){setStatus('No audio file yet. Generate audio locally using the included script.');return;}
    const body=document.querySelector(`[data-audio-id="${CSS.escape(String(x.id))}"] .answer`);
    let text=kind==='question'?x.question:(x.explanation||x.answer||'');
    if(!text.trim()){setStatus('No text available');return;}
    stopSpeech();let my=token;let parts=text.match(/.{1,160}(?:\s|$)/g)||[text];let i=0;
    const next=()=>{if(my!==token)return;if(i>=parts.length){setStatus('Finished browser narration');return;}
      let u=new SpeechSynthesisUtterance(parts[i++]);u.lang='en-US';u.rate=prefs.rate;u.onend=next;u.onerror=()=>setStatus('Browser narration interrupted');window.speechSynthesis.speak(u);};
    fallback={x,kind};setStatus('Browser voice fallback — may stop when screen locks');next();
  }
  async function playItem(x,kind='question'){
    stop();current={x,kind};setTitle((kind==='explanation'?'Explanation: ':'Question: ')+(x.question||x.title));
    player().hidden=false;
    const src=pathFor(x,kind);
    if(!src){speakFallback(x,kind);return;}
    audio.src=src;audio.playbackRate=prefs.rate;updateMediaSession(x);
    try{await audio.play();setStatus('Playing recorded audio · lock screen to test');setPlaying();}
    catch(e){setStatus('Tap Play to allow audio on this device ('+e.name+').');setPlaying();}
  }
  function step(delta){if(!queue.length)return;let i=index+delta;if(i<0||i>=queue.length){setStatus('End of available playlist');return;}index=i;playItem(queue[i],'question');}
  audio.addEventListener('ended',()=>{setPlaying();setStatus('Finished');if(prefs.autoNext)step(1);});
  audio.addEventListener('pause',setPlaying);audio.addEventListener('play',setPlaying);
  audio.addEventListener('error',()=>setStatus('Audio file unavailable or unsupported; check GitHub Pages assets.'));
  function makeButton(label,fn){const b=document.createElement('button');b.type='button';b.textContent=label;b.addEventListener('click',fn);return b;}
  function attach(body,x){
    const p=document.createElement('div');p.className='audio-panel';
    p.append(makeButton('▶ Question',()=>{queue=window.interviewAudioItems?.()||[];index=queue.findIndex(z=>z.kind===x.kind&&z.id===x.id);playItem(x,'question');}),makeButton('▶ Explanation',()=>playItem(x,'explanation')));
    const note=document.createElement('span');note.className='audio-status';note.textContent=pathFor(x,'question')?'Recorded audio available (mobile lock-screen compatible)':'Browser narration fallback (screen-lock not guaranteed)';p.append(note);body.prepend(p);
    body.parentElement?.setAttribute('data-audio-id',String(x.id));
  }
  async function init(){
    try{const r=await fetch('audio/manifest.json',{cache:'no-cache'});if(r.ok)manifest=await r.json();}catch{}
    const root=document.createElement('div');root.id='mobileAudioPlayer';root.className='mobile-audio-player';root.hidden=true;
    root.innerHTML='<div class="mobile-audio-meta"><strong id="mobileAudioTitle">Interview audio</strong><span id="mobileAudioStatus" role="status">Ready</span></div><div class="mobile-audio-controls"><button id="mobileAudioPrev" type="button" aria-label="Previous question">⏮</button><button id="mobileAudioPlay" type="button">▶ Play</button><button id="mobileAudioNext" type="button" aria-label="Next question">⏭</button><button id="mobileAudioStop" type="button">■ Stop</button><label>Speed <select id="mobileAudioSpeed"><option value="0.75">0.75×</option><option value="1">1×</option><option value="1.25">1.25×</option><option value="1.5">1.5×</option><option value="2">2×</option></select></label><label><input type="checkbox" id="mobileAudioAuto"> Auto-next</label></div>';
    document.body.append(root);
    document.getElementById('mobileAudioPrev').onclick=()=>step(-1);
    document.getElementById('mobileAudioNext').onclick=()=>step(1);
    document.getElementById('mobileAudioStop').onclick=stop;
    document.getElementById('mobileAudioPlay').onclick=()=>{
      if(audio.src){if(audio.paused)audio.play().catch(()=>setStatus('Tap again or check audio permissions'));else audio.pause();}
      else if(fallback){if(window.speechSynthesis.paused)window.speechSynthesis.resume();else window.speechSynthesis.pause();}
    };
    const speed=document.getElementById('mobileAudioSpeed');speed.value=String(prefs.rate);speed.onchange=()=>{prefs.rate=Number(speed.value);audio.playbackRate=prefs.rate;save();};
    const auto=document.getElementById('mobileAudioAuto');auto.checked=!!prefs.autoNext;auto.onchange=()=>{prefs.autoNext=auto.checked;save();};
  }
  // DOM creation and manifest load happen early; question cards attach after app data arrives.
  window.interviewAudio={attach,stop};
  document.addEventListener('DOMContentLoaded',init,{once:true});
})();
