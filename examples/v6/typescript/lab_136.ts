// Question #136: Pure vs impure pipes?
// Run: tsc --target ES2022 --module commonjs lab_136.ts && node lab_136.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
const pure=(v:number)=>v*2;assert(pure(3)===pure(3),"pure transformation; avoid expensive impure pipes");
