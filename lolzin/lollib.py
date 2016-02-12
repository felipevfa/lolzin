# coding: utf-8
import logging
import random
import urllib2, json
logger = logging.getLogger(__name__)
rids = [3077, 3048, 3041, 3043, 3044, 3047, 3046, 3122, 3123, 3124, 3025, 2015, 3135, 3134, 3137, 1062, 3024, 3133, 1031, 3139, 3052, 3031, 3033, 3034, 3035, 1063, 1083, 1082, 3140, 3142, 3143, 3144, 3145, 3146, 3040, 3672, 3673, 3671, 3674, 3042, 3036, 3029, 3028, 3026, 3022, 3020, 1018, 3068, 1011, 3812, 3748, 3744, 3742, 3153, 3152, 3151, 3157, 3156, 3155, 3158, 3508, 2047, 2045, 3010, 3504, 3090, 3091, 3094, 1006, 1004, 3751, 3801, 3800, 2049, 3004, 3007, 3006, 3001, 3003, 3057, 3165, 3009, 3008, 2051, 2050, 2053, 3211, 3512, 1038, 1039, 3089, 3085, 3084, 3087, 3086, 1036, 1037, 3083, 3082, 3196, 1042, 3070, 3071, 3072, 3073, 3074, 3075, 1033, 3078, 3170, 3285, 3174, 1027, 1026, 3200, 1029, 1028, 3027, 3060, 3067, 3065, 3222, 1051, 1053, 3108, 1057, 3104, 3105, 3106, 3100, 3101, 3102, 3184, 3185, 3187, 3180, 3181, 1052, 3056, 3053, 3050, 1043, 1041, 3117, 3116, 3115, 3114, 3113, 3112, 3111, 3110, 3197, 1058, 3136, 3191, 3190, 2009, 3198]
loltermos  =  {
	"FlatArmorMod"	: "bônus de armadura", 	
	"FlatAttackSpeedMod"	: "bônus de velocidade de ataque", 	
	"FlatBlockMod"	: "FlatBlockMod", 	
	"FlatCritChanceMod"	: "modificador de Acerto Crítico", 	
	"FlatCritDamageMod"	: "modificador de Dano Crítico", 	
	"FlatEXPBonus"	: "bônus de Experiência", 	
	"FlatEnergyPoolMod"	: "modificador de Energia", 	
	"FlatEnergyRegenMod"	: "bônus de Regeneração de Energia", 	
	"FlatHPPoolMod"	: "bônus de Vida", 	
	"FlatHPRegenMod"	: "bônus de Regeneração de Vida", 	
	"FlatMPPoolMod"	: "bônus de Mana", 	
	"FlatMPRegenMod"	: "bônus de Regeneração de Mana", 	
	"FlatMagicDamageMod"	: "bônus de Poder de Habilidade", 	
	"FlatMovementSpeedMod"	: "bônus de Velocidade de Movimento", 	
	"FlatPhysicalDamageMod"	: "bônus de Dano de Ataque", 	
	"FlatSpellBlockMod"	: "bônus de Resistência Mágica", 	
	"PercentArmorMod"	: "modificador de Penetração de Armadura", 	
	"PercentAttackSpeedMod"	: "bônus de Velocidade de Ataque", 	
	"PercentBlockMod"	: "BLOCK", 	
	"PercentCritChanceMod"	: "bônus de Acerto Crítico", 	
	"PercentCritDamageMod"	: "bônus de Dano Crítico", 	
	"PercentDodgeMod"	: "bonus de dodge", 	
	"PercentEXPBonus"	: "bônus de Experiência", 	
	"PercentHPPoolMod"	: "bônus de Vida", 	
	"PercentHPRegenMod"	: "bônus de Regeneração de Vida", 	
	"PercentLifeStealMod"	: "porcentagem de Roubo de Vida", 	
	"PercentMPPoolMod"	: "bônus de Mana", 	
	"PercentMPRegenMod"	: "bonus de regeneracao de mana %", 	
	"PercentMagicDamageMod"	: "bonus de AP %", 	
	"PercentMovementSpeedMod"	: "bonus de velocidade de movimento", 	
	"PercentPhysicalDamageMod"	: "AD %", 	
	"PercentSpellBlockMod"	: "MR %", 	
	"PercentSpellVampMod"	: "Vampirismo Magico %", 	
	"rFlatArmorModPerLevel"	: "Armadura por nivel", 	
	"rFlatArmorPenetrationMod"	: "Penetracao de armadura", 	
	"rFlatArmorPenetrationModPerLevel"	: "penetracao de armadura por nivel", 	
	"rFlatCritChanceModPerLevel"	: "chance de critico por nivel", 	
	"rFlatCritDamageModPerLevel"	: "dano critico por nivel", 	
	"rFlatDodgeMod"	: "dodge", 	
	"rFlatDodgeModPerLevel"	: "dodge por nivel", 	
	"rFlatEnergyModPerLevel"	: "energia por nivel", 	
	"rFlatEnergyRegenModPerLevel"	: "regeneracao de energia por nivel", 	
	"rFlatGoldPer10Mod"	: "gold per 10", 	
	"rFlatHPModPerLevel"	: "runa", 	
	"rFlatHPRegenModPerLevel"	: "runa", 	
	"rFlatMPModPerLevel"	: "runa", 	
	"rFlatMPRegenModPerLevel"	: "runa", 	
	"rFlatMagicDamageModPerLevel"	: "runa", 	
	"rFlatMagicPenetrationMod"	: "runa", 	
	"rFlatMagicPenetrationModPerLevel"	: "runa", 	
	"rFlatMovementSpeedModPerLevel"	: "runa", 	
	"rFlatPhysicalDamageModPerLevel"	: "runa", 	
	"rFlatSpellBlockModPerLevel"	: "runa", 	
	"rFlatTimeDeadMod"	: "runa", 	
	"rFlatTimeDeadModPerLevel"	: "runa", 	
	"rPercentArmorPenetrationMod"	: "runa", 	
	"rPercentArmorPenetrationModPerLevel"	: "runa", 	
	"rPercentAttackSpeedModPerLevel"	: "runa", 	
	"rPercentCooldownMod"	: "runa", 	
	"rPercentCooldownModPerLevel"	: "runa", 	
	"rPercentMagicPenetrationMod"	: "runa", 	
	"rPercentMagicPenetrationModPerLevel"	: "runa", 	
	"rPercentMovementSpeedModPerLevel"	: "runa", 	
	"rPercentTimeDeadMod"	: "runa", 	
	"rPercentTimeDeadModPerLevel"	: "runa"
}
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

def random_question_item():
	

	while(1):
		item_id = random.choice(rids)
		item = solicitar_item(item_id)
		if(len(item["stats"]) != 0 ):
			break;

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

	return index_ans,lista_final,atributo,item
	


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

def update_user(usuario,resposta):
	usuario.numQuestions += 1
	total = usuario.numQuestions
	if(resposta):
		usuario.cQuestions += 1
	acertos =  usuario.cQuestions
	winrate = 	float(acertos)/total
	if(resposta):
		pts = 10**((winrate+1)**2)
	else:
		pts = -usuario.points*0.075
	winrate = int(100*winrate)/100.0
	if(total<10):
		if(pts>0):
			pts = pts**((total*5+50)/100.0)+acertos
		else:
			pts = -((-pts)**((total*5+50)/100.0))
	usuario.points += pts
	usuario.winrate = winrate
	usuario.league = update_liga(usuario)
	return usuario,int(pts)



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


def update_liga(usuario):
	if(usuario.numQuestions<10):
		return 'unranked'

	pontuacao = usuario.points
	if pontuacao < pontos_de_liga[0] :
		return 'Bronze 5'
	if pontuacao >= pontos_de_liga[6] :
		return 'Faker'
	if pontuacao >= pontos_de_liga[5]:
		return 'Mestre'
	x = 0
	while(pontuacao > pontos_de_liga[x+1]):
		x += 1

	liga = ligas[x]
	resto = pontuacao - pontos_de_liga[x]
	intervalo = pontos_de_liga[x+1] - pontos_de_liga[x]
	intervalo /= 5
	resto  = int(resto/intervalo)
	print resto,intervalo,pontos_de_liga[x],pontos_de_liga[x+1],pontuacao- pontos_de_liga[x]
	return liga + ' '+ str(5-resto)

