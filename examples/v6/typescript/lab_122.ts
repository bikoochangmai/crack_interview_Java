// Question #122: Angular component lifecycle?
// Run: tsc --target ES2022 --module commonjs lab_122.ts && node lab_122.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Lifecycle="created"|"initialized"|"destroyed";const states:Lifecycle[]=["created","initialized","destroyed"];assert(states.at(-1)==="destroyed","lifecycle order");
