let paragraph = document.getElementsByName("p")

paragraph[0].style.color = "red"
paragraph[1].innerHTML = "asdasd"



function changeColor() {
    let h1 = document.getElementsByTagName("h1")
    h1[0].style.color = "red"
}


let h1=document.getElementsByTagName("h1")

let counter=0

function increase(){
    counter++
    h1[0].innerHTML=counter
}