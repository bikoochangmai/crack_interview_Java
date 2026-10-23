// Run with NODE_PATH set to a node_modules directory containing playwright.
const fs=require('node:fs'),path=require('node:path'),http=require('node:http'),assert=require('node:assert/strict');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..');
(async()=>{
 const server=http.createServer((req,res)=>{
  const relative=decodeURIComponent(new URL(req.url,'http://localhost').pathname).replace(/^\//,'')||'index.html';
  const file=path.resolve(root,relative);
  if(!file.startsWith(root+path.sep)){res.writeHead(403).end();return;}
  fs.readFile(file,(err,data)=>{if(err){res.writeHead(404).end();return;}const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'};res.setHeader('Content-Type',types[path.extname(file)]||'application/octet-stream');res.end(data);});
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 let browser;
 try{
  browser=await chromium.launch({headless:true,channel:process.env.PLAYWRIGHT_CHANNEL||'msedge'});
  const page=await browser.newPage({viewport:{width:1440,height:1000}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  const base='http://127.0.0.1:'+server.address().port;
  await page.goto(base);await page.waitForFunction(()=>document.getElementById('count').textContent.includes('386'));
  const questions=JSON.parse(fs.readFileSync(path.join(root,'data/questions.json'),'utf8'));
  const lessons=questions.filter(q=>q.category.startsWith('System Design')||q.category.startsWith('Design Patterns'));
  assert.equal(lessons.length,34);
  assert(questions.find(q=>q.id===243).contentBlocks.some(b=>b.text.includes('PUBLIC_SHORT_ORIGIN')));
  for(const q of lessons){
   assert.equal(q.walkthroughSteps.length,4);
   await page.selectOption('#category',q.category);
   const card=page.locator('#questions details').filter({has:page.locator('summary .num',{hasText:'#'+q.id})});
   await card.locator('summary').click();
   const image=card.locator('.design-figure img');await image.scrollIntoViewIfNeeded();
   await image.evaluate(img=>img.decode());
   for(const tutorialImage of await card.locator('.tutorial-figure img').all()){await tutorialImage.scrollIntoViewIfNeeded();await tutorialImage.evaluate(img=>img.decode());assert((await tutorialImage.getAttribute('alt')).length>5);}
   assert.equal(await image.evaluate(img=>img.naturalWidth),960);
   if(q.guidePath)assert.equal(await card.locator('a').filter({hasText:'Beginner glossary'}).getAttribute('href'),q.guidePath);
   if(q.lessonSections)assert((await card.innerText()).includes(q.lessonSections[0].explanation));
   await card.locator('.design-step-buttons button').nth(3).click();
   assert.equal(await card.locator('.design-step-buttons button').nth(3).getAttribute('aria-pressed'),'true');
   assert((await card.locator('.design-walkthrough').innerText()).includes(q.walkthroughSteps[3].explanation));
   await card.locator('summary').click();
  }
  // Inspect every diagram's text bounds; catch clipped labels without network dependencies.
  const diagrams=['docs/system-design/diagrams','docs/design-patterns/diagrams'].flatMap(dir=>fs.readdirSync(path.join(root,dir)).filter(f=>f.endsWith('.svg')).map(f=>dir+'/'+f));
  for(const file of diagrams){
   await page.goto(base+'/'+file);
   const overflow=await page.locator('svg').evaluate(svg=>{const v=svg.viewBox.baseVal;return [...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height;}).map(t=>t.textContent);});
   assert.deepEqual(overflow,[],file+' clipped text');
  }
  await page.goto(base);await page.waitForFunction(()=>document.getElementById('count').textContent.includes('386'));
  await page.selectOption('#category',lessons.find(q=>q.id===243).category);
  await page.locator('#questions details').first().locator('summary').click();
  await page.locator('.design-figure').first().scrollIntoViewIfNeeded();
  if(process.env.DESIGN_SCREENSHOT_DIR){await page.screenshot({path:path.join(process.env.DESIGN_SCREENSHOT_DIR,'system-design-desktop.png')});}
  await page.setViewportSize({width:390,height:844});await page.locator('.design-walkthrough').first().scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth),'mobile page overflows');
  await page.locator('.design-step-buttons button').nth(1).click();
  if(process.env.DESIGN_SCREENSHOT_DIR){await page.screenshot({path:path.join(process.env.DESIGN_SCREENSHOT_DIR,'system-design-mobile.png')});}
  assert.deepEqual(errors,[]);
  console.log('PASS: 34 lesson images and step controls, 46 SVG text bounds, mobile width, no browser errors.');
 }finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(e=>{console.error(e);process.exitCode=1;});
