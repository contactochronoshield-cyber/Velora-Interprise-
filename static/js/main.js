
document.addEventListener("DOMContentLoaded",function(){

setTimeout(function(){

let loader=document.getElementById("loader");

if(loader){

loader.style.display="none";

}

},3000);

});

/* ============================= */
/* RELOJ */
/* ============================= */

function updateClock(){

const now=new Date();

const options={

hour:"2-digit",

minute:"2-digit",

second:"2-digit",

day:"2-digit",

month:"short",

year:"numeric"

};

const clock=document.getElementById("clock");

if(clock){

clock.innerHTML=now.toLocaleString("es-CO",options);

}

}

setInterval(updateClock,1000);

/* ============================= */
/* EFECTO TARJETAS */
/* ============================= */

document.addEventListener("mouseover",e=>{

if(e.target.classList.contains("card")){

e.target.style.transform="translateY(-8px)";

e.target.style.boxShadow="0 0 35px rgba(0,191,255,.5)";

}

});

document.addEventListener("mouseout",e=>{

if(e.target.classList.contains("card")){

e.target.style.transform="translateY(0px)";

e.target.style.boxShadow="0 0 15px rgba(0,191,255,.2)";

}

});

/* ============================= */
/* MENÚ */
/* ============================= */

document.querySelectorAll(".sidebar a").forEach(link=>{

link.addEventListener("click",function(){

document.querySelectorAll(".sidebar a").forEach(a=>{

a.classList.remove("active");

});

this.classList.add("active");

});

});

/* ============================= */
/* MENSAJE */
/* ============================= */

console.log("VELORA ENTERPRISE");

console.log("Chrono Shield Networks");

console.log("Enterprise SaaS");

