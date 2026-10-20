// Question #126: Subject vs BehaviorSubject vs ReplaySubject?
// Run: tsc --target ES2022 --module commonjs lab_126.ts && node lab_126.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
class Behavior<T>{constructor(public current:T){}next(v:T){this.current=v}}const s=new Behavior(0);s.next(2);assert(s.current===2,"latest value semantics; not RxJS");
