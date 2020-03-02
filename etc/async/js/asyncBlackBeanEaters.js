function asyncBlackBeanEaters (name) {
    console.log(`Deliver to ${name}`);

    http.get("http://localhost:3000/eat-noodle-rand",   // server spends 1-5 seconds randomly
        function() {
            console.log(`${name} eating completed`);
        }
    );
}

let eaters = ["yu", "kim", "moon", "kim2", "don"];
for (let i = 0; i < eaters.length; i++) {
    asyncBlackBeanEaters(eaters[i]);
}
