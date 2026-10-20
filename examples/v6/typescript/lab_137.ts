// Question #137: TypeScript interface vs type alias?
// Run: tsc --target ES2022 --module commonjs lab_137.ts && node lab_137.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
interface Finding{id:string};type Result=Finding|{error:string};const x:Result={id:"1"};assert("id" in x,"interface extension vs type union");
