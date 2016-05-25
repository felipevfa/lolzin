# coding: utf-8
import logging, random, urllib2, json
logger = logging.getLogger(__name__)
from dict_loltermos import loltermos,rids



class api():	

	ratios = [0.3,0.4,0.5,0.6,0.7,0.8,0.9]
	ligas = [
		'Bronze',
		'Prata',
		'Ouro',
		'Platina',
		'Diamante',
		'Mestre',
		'Faker'
	]
	pontos_de_liga = []
	for i in ratios:
		value = 10**((1+i)**2)
		value /= 0.075
		pontos_de_liga.append(value)


	@staticmethod
	def random_champion_background():
		"""pega a lista de todos os champions, e da o link da splash. 
		processo mt pesado, facilmente otimizavel atraves de cache ou variavel local"""
		CHAMPIONS = solicitar_campeoes()
		champ_name = str(random.choice(list(CHAMPIONS['data'])))
		lista_skin = CHAMPIONS['data'][champ_name]['skins']
		skin_number = str(random.choice(lista_skin)['num'])
		background_link = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + champ_name + "_" + skin_number + ".jpg"
		return background_link
	
	@staticmethod
	def random_item():
		while(1):
			item_id = random.choice(rids)
			item = solicitar_item(item_id)
			if(len(item["stats"]) != 0 ):
				break;
		item_img_link = "http://ddragon.leagueoflegends.com/cdn/5.23.1/img/item/"+str(item["id"])+".png"
		item['item_img_link'] = item_img_link
		return item
	@staticmethod
	def random_item_question(item):
		"""gera um dicionario para o contexto da view, com o item,
		imagem, alternativas aleatorias e resposta correta.
		pode ser otimizado ocultando do html a opcao correta"""
		

		stats = item["stats"]
		atributo = random.choice(stats.keys())
		ans = stats[atributo]
		
		#	numero de possiveis alternativas geradas eh (alcance-1)*2
		alcance = 5

		#	base de variacao das alternativas, alternativas geradas serao
		#	ans + base*x, -alcance < x < alcance
		base = 1

		#	se ans < 1, eh uma resposta fracionaria, 
		#	deve portanto ser tranformada em int para evitar erros de float
		fracionario = 0


		
		if(ans < 1):
			ans = int(100.0*ans)
			fracionario = 1
		else:
			ans = int(ans)

		#	< 10%
		#   0 < ans <= 0.1 		
		#	move speed
		if(ans <= 12 and fracionario):
			base = 1
		
		#	10% < x <= 100%
		#	0.1 < x <= 1 		
		#	life steal, spell vamp, atk spd, crit chance
		elif(ans <= 100 and fracionario):
			base = 5
			alcance = 4
		
		#	1 < x <= 15
		#	bonus ad tier 1
		elif(ans <= 16):
			if(ans % 5 == 0):
				base = 5
			else:
				base = 1
			alcance = 4

		#	15 < x <= 150
		#	tier 2 ad, bonus ap, armadura, mr
		elif(ans <= 120):
			base = 5

		#	150 < x <= 300
		#	bonus HP tier 1
		elif(ans <= 300):
			base = 50
			alcance = 3

		#	300 < x <= 1000
		elif(ans <= 1000):
			base = 100
			alcance = 3

		opcoes_maiores = range(1,alcance)
		opcoes_menores = range(1,alcance)


		opcoes_maiores = map(lambda x:x*base+ans,opcoes_maiores)
		opcoes_menores = map(lambda x:ans-x*base,opcoes_menores)
		
		opcoes_menores = filter(lambda x: x>0,opcoes_menores)
		if(fracionario):
			opcoes_maiores = filter(lambda x: x<=100,opcoes_maiores)
		
		lista_final = opcoes_maiores + opcoes_menores

		#	randomizando as alternativas da questao
		random.shuffle(lista_final)
		lista_final = [ans] + lista_final[0:3]

		#	randomizando a posicao da alternativa correta
		random.shuffle(lista_final)

		#	encontrando a posicao da resposta correta
		index_ans = lista_final.index(ans)

		#	caso fracionario
		#	resposta em %, concatenar '%'
		if(fracionario):
			for i in range(len(lista_final)):
				lista_final[i] = str(lista_final[i]) + '%'
		
		#	indice da resposta correta, lista com opcoes, atributo em questao, dic do item escolhido
		finaldic = {
			'item_correto':index_ans,
			'opts': lista_final,
			'atributo': loltermos[atributo],
		}
		return finaldic



def solicitar_campeoes():
	logger.debug('solicitar_campeoes')
	api_com_skins = 'https://global.api.pvp.net/api/lol/static-data/br/v1.2/champion?champData=skins&api_key=aefffeaf-785b-4fff-8487-5c5f38f01870'
	consulta = json.load(urllib2.urlopen(api_com_skins))	
		
	return consulta


def solicitar_item(id):
	api_key = 'aefffeaf-785b-4fff-8487-5c5f38f01870'
	#get_item_by_id(id)
	prefixo = 'https://global.api.pvp.net/api/lol/static-data/br/v1.2/item/'
	#get_item_by_id(id).get_stats()
	posfixo= '?itemData=stats&'
	url = prefixo+str(id)+posfixo+'api_key=' + api_key
	response = urllib2.urlopen(url)
	data_dic = json.load(response)
	return data_dic


win_gif = ["http://i.imgur.com/QRUPiHQ.gif",
	"http://cdn.makeagif.com/media/11-02-2015/WIN_P1.gif",
	"https://45.media.tumblr.com/15ec57cd43b0eef16286169236a85192/tumblr_nz5aeuuV8M1v1ncd6o1_500.gif",
	"http://img2.wikia.nocookie.net/__cb20130325232219/leagueoflegends/images/3/3b/Trundle_Dance.gif"]

fail_gif = ['https://49.media.tumblr.com/87033a4730095aeaa1f6d4b24ac3c374/tumblr_n65ag40I9K1rkinvho1_400.gif',
	"http://i.imgur.com/yPQrs65.jpg",
	"http://49.media.tumblr.com/bf73435cd9a1b1ca4abf2264b3736242/tumblr_mgu8gwrz3b1rtqiuqo1_1280.gif",
	"http://img3.wikia.nocookie.net/__cb20131119031239/creepypasta/images/thumb/1/12/You-tried.gif/479px-You-tried.gif",
	"http://st.elohell.net/public/chill/4e27038dcfad146c87348f429b73a7ee.gif",
	"http://i.imgur.com/kPxoY.gif",
	"http://st.elohell.net/public/chill/ed44674265346bea7f1e771cff764d6f.gif"]
profile_background = {
	'unranked' : None,
	'Bronze' : None,
	'Prata' : None,
	'Ouro' : "http://www.latoro.com/wallpapers/games/19082-desktop-wallpapers-league-of-legends.jpg",
	'Platina' : "http://ppsparents.com/wp-content/uploads/2015/12/wallpapers-hd-1920x1080-league-of-legends-cool-with-photo-of-wallpapers-hd-photography-new-on-wallpaper-gallery.jpg",
	'Diamante' : "http://efondos.com/wp-content/uploads/2015/04/league_of_legends_diamond_badge_wallpaper_hd.jpg",
	'Mestre' : "http://www.ozonegaming.com/upload/images/ozoneXpeke_1920x1080.jpg",
	'Faker' : "http://cdn2.game4v.com/2015/04/faker4.jpg"
	}