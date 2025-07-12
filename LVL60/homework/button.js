const p1=document.getElementById("paragraph1")
const p2=document.getElementById("paragraph2")
const btn1=document.getElementById("add")
const btn2=document.getElementById("change")

btn1.addEventListener("click", function(){
    p1.innerHTML="text added"
})


btn2.addEventListener("click",function(){
    p2.innerHTML="<b>Deme</b>"
})