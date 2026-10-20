// Question #133: Angular authentication and token storage?
// Run: tsc --target ES2022 --module commonjs lab_133.ts && node lab_133.js
// Pure TypeScript demo: real Angular/RxJS integration requires Angular dependencies.
function assert(condition:boolean,message:string):void{if(!condition)throw new Error(message);console.log("PASS: "+message)}
const tokenStore:{accessToken?:string}={};assert(tokenStore.accessToken===undefined,"no hardcoded tokens; prefer secure session design");
