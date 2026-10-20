// Question #138: Generics, union and discriminated unions?
// Run: tsc --target ES2022 --module commonjs lab_138.ts && node lab_138.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Result<T>={ok:true;data:T}|{ok:false;error:string};const r:Result<number>={ok:true,data:42};assert(r.ok&&r.data===42,"discriminated union narrowing");
