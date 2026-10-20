// Question #134: Content projection vs ViewChild?
// Run: tsc --target ES2022 --module commonjs lab_134.ts && node lab_134.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Slot={content:string;childId:string};const s:Slot={content:"Projected content",childId:"table"};assert(s.content.length>0,"projection vs child reference model");
