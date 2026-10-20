// Question #141: Unit tests and component integration tests?
// Run: tsc --target ES2022 --module commonjs lab_141.ts && node lab_141.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
const total=(a:number,b:number)=>a+b;assert(total(2,3)===5,"unit test assertion; Angular TestBed required for component integration");
