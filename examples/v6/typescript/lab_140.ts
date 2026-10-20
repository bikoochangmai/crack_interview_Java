// Question #140: State management service vs NgRx?
// Run: tsc --target ES2022 --module commonjs lab_140.ts && node lab_140.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
class Store{private count=0;dispatch(){this.count++}select(){return this.count}}const s=new Store();s.dispatch();assert(s.select()===1,"simple service store; NgRx adds reducers/effects");
