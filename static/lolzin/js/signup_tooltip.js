"use strict";

$(document).ready(function () {
	var nick = $("#id_nick"),
		email = $("#id_identifier"),
		pass1 = $("#id_password1"),
		pass2 = $("#id_password2");

	nick.attr("title", "Nome usado no login. Este é o nome pelo qual os outros usuários do site verão você.");
	nick.tooltip();
	email.attr("title", "E-mail único para cada usuário.");
	email.tooltip();
	pass1.attr("title", "Recomendamos que você NÃO use a mesma senha do jogo.");
	pass1.tooltip();
	pass2.attr("title", "Recomendamos que nao use copiar+colar =)");
	pass2.tooltip();

});