// Run with NODE_PATH pointing to the bundled node_modules containing playwright.
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..');
(async()=>{
 const server=http.createServer((req,res)=>{
  const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  const file=path.resolve(root,pathname.replace(/^\//,'')||'index.html');
  if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return;}
  fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end();return;}const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'};res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');res.end(data);});
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));let browser;
 try{
  browser=await chromium.launch({headless:true,channel:process.env.PLAYWRIGHT_CHANNEL||'msedge'});
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  const base='http://127.0.0.1:'+server.address().port;
  await page.goto(base);await page.waitForFunction(()=>document.getElementById('count').textContent.startsWith('Showing'));
  assert.equal(await page.locator('#navTree a[href="docs/generative-ai/index.html"]').count(),1);
  await page.selectOption('#category','AI Engineering — Illustrated Generative AI Notes');
  await page.locator('#questions details summary').click();
  const answer=page.locator('#questions .answer');
  assert.equal(await answer.locator('.ai-topic-heading').count(),20);
  assert.equal(await answer.locator('table').count(),55);
  assert.equal(await answer.locator('.tutorial-figure img').count(),39);
  const inline=await answer.innerText();
  assert(inline.includes('Self-attention allows the model to look at tokens'));
  assert(inline.includes('BitsAndBytes'));
  assert(!inline.includes('Open the single-page illustrated guide and select this subsection'));
  assert(!inline.includes('Source page'));
  assert(!inline.includes('What is it? — Concept'));
  await page.setViewportSize({width:390,height:844});
  await answer.locator('.ai-mobile-flow').first().scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'inline mobile notes overflow');
  if(process.env.DESIGN_SCREENSHOT_DIR)await page.screenshot({path:path.join(process.env.DESIGN_SCREENSHOT_DIR,'ai-notes-inline-mobile.png')});
  await page.setViewportSize({width:1440,height:1000});
  await page.locator('.notes-guide-link').click();
  await page.waitForURL('**/docs/generative-ai/index.html');
  assert.equal(await page.locator('.note-section').count(),20);
  assert(!(await page.locator('main').innerText()).toLowerCase().includes('source page'));
  assert.equal(await page.locator('figure img').count(),39);
  const source=JSON.parse(fs.readFileSync(path.join(root,'data/ai-study-notes.json'),'utf8'));
  assert.equal(await page.locator('table').count(),source.flatMap(p=>p.blocks).filter(b=>b.type==='table').length);
  assert(!(await page.locator('body').textContent()).toLowerCase().includes('rahul yadav'));
  for(const img of await page.locator('figure img').all()){
   await img.scrollIntoViewIfNeeded();await img.evaluate(image=>image.decode());
   assert.equal(await img.evaluate(image=>image.naturalWidth),960);
  }
  await page.locator('#notes-search').fill('LoRA');assert(await page.locator('.note-section:visible').count()>=3);
  await page.locator('#notes-search').fill('not-a-real-topic-xyz');assert.equal(await page.locator('.note-section:visible').count(),0);
  await page.locator('#show-all').click();assert.equal(await page.locator('.note-section:visible').count(),20);
  const check=page.locator('[data-check="page-8"]');await check.check();
  await page.reload();assert(await check.isChecked());assert((await page.locator('#notes-status').innerText()).includes('1 sections studied'));
  await page.locator('[data-check="revision-0"]').check();await page.reload();assert(await page.locator('[data-check="revision-0"]').isChecked());
  await page.locator('#notes-search').fill('LoRA');await page.evaluate(()=>{location.hash='#page-02';});
  await page.waitForFunction(()=>!document.getElementById('page-02').hidden);
  assert.equal(await page.locator('#notes-search').inputValue(),'');
  if(process.env.DESIGN_SCREENSHOT_DIR){await page.locator('#page-08').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(process.env.DESIGN_SCREENSHOT_DIR,'ai-notes-desktop.png')});}
  await page.setViewportSize({width:390,height:844});
  for(const section of await page.locator('.note-section').all()){
   await section.scrollIntoViewIfNeeded();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'mobile document overflow');
  }
  await page.locator('#page-08 figure').first().scrollIntoViewIfNeeded();
  if(process.env.DESIGN_SCREENSHOT_DIR){await page.screenshot({path:path.join(process.env.DESIGN_SCREENSHOT_DIR,'ai-notes-mobile.png')});}
  await page.locator('#notes-search').fill('LoRA');await page.emulateMedia({media:'print'});
  assert.equal(await page.locator('.note-section:visible').count(),20);await page.emulateMedia({media:'screen'});
  for(const block of source.flatMap(p=>p.blocks).filter(b=>b.path)){
   await page.goto(base+'/'+block.path);
   const overflow=await page.locator('svg').evaluate(svg=>{const v=svg.viewBox.baseVal;return [...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height;}).map(t=>t.textContent);});
   assert.deepEqual(overflow,[],block.path+' clipped SVG text');
  }
  assert.deepEqual(errors,[]);
  console.log('PASS: AI navigation, all 20 subsections, tables, 39 loaded SVGs, search/reset, hash navigation, persistent checkboxes, print visibility, mobile width and SVG text bounds.');
 }finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(e=>{console.error(e);process.exitCode=1;});
