
console.log("Velora Enterprise Loaded");

setInterval(function(){

fetch("/api/status")

.then(r=>r.json())

.then(function(data){

document.title="Velora | "+data.status;

});

},5000);

