// Question #128: Async pipe and subscription cleanup?
// Run: tsc --target ES2022 --module commonjs lab_128.ts && node lab_128.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
class Subscription{closed=false;unsubscribe(){this.closed=true}}const s=new Subscription();s.unsubscribe();assert(s.closed,"cleanup model; Angular async pipe unsubscribes automatically");
