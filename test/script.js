
// let name="ansdjads"

// for(let i=0; i <name.length; i++){
//     console.log(i)
// }


document.getElementById("click").addEventListener("click", function () {
    let rain = prompt("is it raining?");

    while (rain === "no") {
        rain = prompt("let me ask again is it raining?");
    }

    if (rain === "yes") {
        alert("YES BRO I LOVE RAIN");
    } else {
        alert("you are weird ;-; bye!..");
    }
});
