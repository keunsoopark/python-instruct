function asyncBlackBeanTimer (seconds) {
    console.log("Blackbean delivered");

    setTimeout(
        function() {    // callback function
            console.log("Eating completed");
        },
        seconds * 1000
    );

    console.log("Delivery guy left")
}

asyncBlackBeanTimer(1);

// node asyncBlackBeanTimer.js: to run
// result:
// Balckbean delivered
// Delivery guy left
// Eating completed