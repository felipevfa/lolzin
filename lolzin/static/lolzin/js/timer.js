"use strict";

$.fn.exists = function() {
	return this.length > 0 ? this : false;
}

var reloadPage = function (unit, timeLeft, totalTime) {
	console.log("Time Left: " + timeLeft);

	if (timeLeft == 0) {
		timer.TimeCircles().destroy();
		location.reload();
	}
};

$(document).ready(function() {
	var timer = $("#timer");

	if (timer.exists()) {
		timer.TimeCircles(
		{ 
			time: { 
				Days: { show: false },
				Hours: { show: false },
				Minutes: { show: false},
				Seconds: { show: true, text: "", color: "#3399FF" }
			},
			start_angle: 360,
			count_past_zero: false,
			total_duration: 20
		});

	
		setInterval(function() {
			if (timer.TimeCircles().getTime() <= 0) {
				location.reload(true);
			}
		}, 1000);
	}
});