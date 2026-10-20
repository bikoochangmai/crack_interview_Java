// Question #130: Custom validators and async validators?
// Run: tsc --target ES2022 --module commonjs lab_130.ts && node lab_130.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
type Validation={valid:boolean;errors:string[]};const validate=(v:string):Validation=>({valid:v.length>=3,errors:v.length>=3?[]:["minlength"]});assert(!validate("a").valid,"custom validator");
