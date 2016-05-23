/** LOLZIN GENERAL.JS 1.0 
 *  Esse arquivo contém funções genéricas que devem estar ativas em todas as páginas de modo
 *  a manter a consistência das funcionalidades da aplicação. 
*/

$(document).ready(function() {
	var adjustQuestionCardBackground = function () {
		var cardHeight = 0;

		cardHeight = $('.question-card').height();

		$('.question-card::before').height(cardHeight);
	};

	/* Inicialização da Navegação Mobile */
	$('.button-collapse').sideNav();

	$("main").has("section.section-wrapper").css("min-height", "calc(100vh - 106px)");

	adjustQuestionCardBackground();
});
