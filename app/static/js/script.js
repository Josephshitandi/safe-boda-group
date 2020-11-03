var startingMinute;
var start;
var length;
var end;
var countDown;
var now;
var remaining;
var minutes;
var seconds;
var pauseTime;
var pauseLength;

//show page content when loaded
$(document).ready(function () {
    startingMinute = 59;
    $('#display').html('59:00');
});

function display() {
    $('#display').empty().html(startingMinute + ':00');
}

//user adds minutes
$('#add').on('click', function () {
    startingMinute = startingMinute + 1;
    display();
});

//user tsubtracts minutes
$('#subtract').on('click', function () {
    if (startingMinute > 1) {
        startingMinute = startingMinute - 1;
        display();
    }
});

// update each and every count down
function secondCount() {
    countDown = setInterval(function () {

        // Get current time
        now = $.now();

        // difference between current time user input minutes
        remaining = end - now;

        // calculations for days, hours, minutes and seconds
        minutes = Math.floor((remaining % (1000 * 60 * 60)) / (1000 * 60));
        seconds = Math.round((remaining % (1000 * 60)) / 1000);

        // Display the result 

        if (seconds == 60) {
            document.getElementById("display").innerHTML = "1:00";
        }

        else if (seconds < 10) {
            document.getElementById("display").innerHTML = minutes + ":0" + seconds;
        }

        else document.getElementById("display").innerHTML = minutes + ":" + seconds;


        // If the count down is finished and end text is written
        if (remaining < 0) {
            clearInterval(countDown);
            document.getElementById("display").innerHTML = "END";
        }


    }, 1000);

}

//user starts or resumes
$('#start').on('click', function () {

    //start
    if (isNaN(pauseTime)) {
        start = $.now();
        length = startingMinute * 60 * 1000;
        end = start + length;
        secondCount();
    }

    //resume
    else {
        start = $.now();
        end = start + pauseLength;
        secondCount();
    }

});

//user pauses
$('#pause').on('click', function () {
    pauseTime = $.now();
    pauseLength = end - pauseTime;
    clearInterval(countDown);

});

//user resets
$('#stop').on('click', function () {
    clearInterval(countDown);
    startingMinute = 59;
    display();
    pauseTime = NaN;
});