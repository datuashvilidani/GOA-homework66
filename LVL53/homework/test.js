// let name="Danieli"

// for(let i=0;i<name.length;i++){
//     console.log(name[i]);
// }


for (let i = 0; i < 30; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FIZZBUZZ");
    } else if (i % 3 === 0) {
        console.log("FIZZ");
    } else if (i % 5 === 0) {
        console.log("BUZZ");
    }
}