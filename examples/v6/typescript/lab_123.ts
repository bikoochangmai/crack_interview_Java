// Question #123: Standalone components vs NgModules?
// Run: tsc --target ES2022 --module commonjs lab_123.ts && node lab_123.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Standalone={standalone:true;imports:string[]};const c:Standalone={standalone:true,imports:["CommonModule"]};assert(c.standalone,"standalone metadata concept");
