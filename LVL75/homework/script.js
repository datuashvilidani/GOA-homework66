const car = {
    model: "Ferrari",
    milage: 34000,
    year: 2019,
    condition: "good",

    checkCondition: function (condition) {
        if (condition === "good" || condition === "bad") {
            console.log(`car is in ${condition} condition`);
        }
    }
};