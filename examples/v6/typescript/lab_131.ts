// Question #131: Route guards and lazy loading?
// Run: tsc --target ES2022 --module commonjs lab_131.ts && node lab_131.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Route={path:string;authorized:boolean};const r:Route={path:"/admin",authorized:false};assert(!r.authorized,"client guard is UX; server must authorize");
