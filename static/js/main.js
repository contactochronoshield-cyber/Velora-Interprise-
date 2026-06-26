
function clock(){

const now=new Date();

document.getElementById("clock").innerHTML=

now.toLocaleString();

}

setInterval(clock,1000);

clock();

async function refreshStatus(){

try{

const r=await fetch("/api/status");

const d=await r.json();

console.log(d);

}catch(e){}

}

setInterval(refreshStatus,5000);

