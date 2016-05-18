"use strict";

$(document).ready(function() {

	$(document.body).keydown(function (e) {
		

		var keyNum;

		if (window.event) {
			keyNum = e.keyCode;
		}
		else {
			if (e.which) {
				keynum = e.which;
			}
		}

		switch(keyNum) {
			case 49:
				$("#options-form input:nth-child(2)").prop("checked", true);
				break;
			case 50:
				$("#options-form input:nth-child(5)").prop("checked", true);
				break;
			case 51:
				$("#options-form input:nth-child(8)").prop("checked", true);
				break;
			case 52:
				$("#options-form input:nth-child(11)").prop("checked", true);
				break;
			case 84:
				$("#options-form input[value = 1]").prop("checked", true);
				break;

			case 13:
				var e = $.Event('click');
				$("#answer-button").trigger(e);
			default:
				break;
		}
	});
});