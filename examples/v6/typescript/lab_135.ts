// Question #135: trackBy / @for track and rendering?
// Run: tsc --target ES2022 --module commonjs lab_135.ts && node lab_135.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
const rows=[{id:"a",name:"A"},{id:"b",name:"B"}];assert(new Set(rows.map(r=>r.id)).size===rows.length,"stable track keys");
