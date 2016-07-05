/** LOLZIN GENERAL.JS 1.0 
 *  Esse arquivo contém funções genéricas que devem estar ativas em todas as páginas de modo
 *  a manter a consistência das funcionalidades da aplicação. 
*/

var adjustQuestionCardBackground = function () {
	var cardHeight = 0;

	cardHeight = $('.question-card').height();

	$('.question-card::before').height(cardHeight);
};

var adjustSectionSize = function () {
	var main = $("main");

	main.has("section.section-wrapper").css("min-height", "calc(100vh - 106px)");
};

var setKeyboardShortcuts = function () {
	$(document.body).on("keydown", function(e) {
	
		var keyNum = 49;

		if (window.event) {
			keyNum = e.keyCode;
		}
		else {
			if (e.which) {
				keyNum = e.which;
			}
		}

		switch(keyNum) {
			case 49:
				$("#question-form #option-1").prop("checked", true);
				break;
			case 50:
				$("#question-form #option-2").prop("checked", true);
				break;
			case 51:
				$("#question-form #option-3").prop("checked", true);
				break;
			case 52:
				$("#question-form #option-4").prop("checked", true);
				break;
			case 84:
				$("#question-form input[value=1]").prop("checked", true);
				break;

			case 13:
				var event = $.Event('click');
				$("#answer-button").trigger(event);
				break;

			default:
				break;
		}
	}); 
};

$(document).ready(function() {
	/* Inicialização da Navegação Mobile */
	$('.button-collapse').sideNav();

	adjustSectionSize();
	adjustQuestionCardBackground();
	
	if ($("#question-form").length > 0) {
		setKeyboardShortcuts();
	}
});
