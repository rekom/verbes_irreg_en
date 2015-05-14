# -*- coding: utf-8 -*-
import random
counter = 0
score = 0
lst = []

# création d'un dictionnaire avec verbes et traduction Française,
# une liste dans un dictionnaire

verbes = {
"abide":["abode","abode","respecter / se conformer à"],
"arise":["arisen","arisen","survenir"],
"awake":["awoken","awoken","se réveiller"],
"be":["been","been","être"],
"bear":["borne / born","borne / born","porter / supporter / naître"],
"beat":["beaten","beaten","battre"],
"become":["become","become","devenir"],
"beget":["begotten","begotten","engendrer"],
"begin":["begun","begun","commencer"],
"bend":["bent","bent","plier / se courber"],
"bereave":["bereft / bereaved","bereft / bereaved","déposséder / priver"],
"bet":["bet","bet","parier"],
"bid":["bid / bidden","bid / bidden","offrir"],
"bleed":["bled","bled","saigner"],
"blow":["blown","blown","souffler / gonfler"],
"break":["broken","broken","casser"],
"breed":["bred","bred","élever (des animaux)"],
"bring":["brought","brought","apporter"],
"broadcast":["broadcast","broadcast","diffuser / émettre"],
"build":["built","built","construire"],
"burn":["burnt / burned","burnt / burned","brûler"],
"burst":["burst","burst","éclater"],
"buy":["bought","bought","acheter"],
"can":["could","could","pouvoir"],
"cast":["cast","cast","jeter / distribuer (rôles)"],
"catch":["caught","caught","attraper"],
"chide":["chiden","chiden","gronder"],
"choose":["chosen","chosen","choisir"],
"cling":["clung","clung","s'accrocher"],
"clothe":["clad / clothed","clad / clothed","habiller / recouvrir"],
"come":["come","come","venir"],
"cost":["cost","cost","coûter"],
"creep":["crept","crept","ramper"],
"cut":["cut","cut","couper"],
"deal":["dealt","dealt","distribuer"],
"dig":["dug","dug","creuser"],
"dive":["dived / dove","dived / dove","plonger"],
"do":["done","done","faire"],
"draw":["drawn","drawn","dessiner / tirer"],
"dream":["dreamt / dreamed","dreamt / dreamed","rêver"],
"drink":["drunk","drunk","boire"],
"drive ":["driven","driven","conduire"],
"dwell":["dwelt / dwelled","dwelt / dwelled","habiter"],
"eat":["eaten","eaten","manger"],
"fall":["fallen","fallen","tomber"],
"feed":["fed","fed","nourrir"],
"feel":["felt","felt","se sentir / ressentir"],
"fight":["fought","fought","se battre"],
"find":["found","found","trouver"],
"flee":["fled","fled","s'enfuir"],
"fling":["flung","flung","lancer"],
"fly":["flown","flown","voler"],
"forbid":["forbidden","forbidden","interdire"],
"forecast":["forecast","forecast","prévoir"],
"foresee":["foreseen","foreseen","prévoir / présentir"],
"forget":["forgotten / forgot","forgotten / forgot","oublier"],
"forgive":["forgiven","forgiven","pardonner"],
"forsake":["forsaken","forsaken","abandonner"],
"freeze":["frozen","frozen","geler"],
"get":["gotten / got","gotten / got","obtenir"],
"give":["given","given","donner"],
"go":["gone","gone","aller"],
"grind":["ground","ground","moudre / opprimer"],
"grow":["grown","grown","grandir / pousser"],
"hang":["hung","hung","tenir / pendre"],
"have":["had","had","avoir"],
"hear":["heard","heard","entendre"],
"hide":["hidden","hidden","cacher"],
"hit":["hit","hit","taper / appuyer"],
"hold":["held","held","tenir"],
"hurt":["hurt","hurt","blesser"],
"keep":["kept","kept","garder"],
"kneel":["knelt / kneeled","knelt / kneeled","s'agenouiller"],
"know":["known","known","connaître / savoir"],
"lay":["laid","laid","poser"],
"lead":["led","led","mener / guider"],
"lean":["leant / leaned","leant / leaned","s'incliner / se pencher"],
"leap":["leapt / leaped","leapt / leaped","sauter / bondir"],
"learn":["learnt","learnt","apprendre"],
"leave":["left","left","laisser / quitter / partir"],
"lend":["lent","lent","prêter"],
"let":["let","let","permettre / louer"],
"lie":["lain","lain","s'allonger"],
"light":["lit / lighted","lit / lighted","allumer"],
"lose":["lost","lost","perdre"],
"make":["made","made","fabriquer"],
"mean":["meant","meant","signifier"],
"meet":["met","met","rencontrer"],
"mow":["mowed / mown","mowed / mown","tondre"],
"offset":["offset","offset","compenser"],
"overcome":["overcome","overcome","surmonter"],
"partake":["partaken","partaken","prendre part à"],
"pay":["paid","paid","payer"],
"plead":["pled / pleaded","pled / pleaded","supplier / plaider"],
"preset":["preset","preset","programmer"],
"prove":["proven / proved","proven / proved","prouver"],
"put":["put","put","mettre"],
"quit":["quit","quit","quitter"],
"read":["read","read","lire"],
"relay":["relaid","relaid","relayer"],
"rend":["rent","rent","déchirer"],
"rid":["rid","rid","débarrasser"],
"ride":["ridden","ridden","monter (vélo, cheval)"],
"ring":["rung","rung","sonner / téléphoner"],
"rise":["risen","risen","lever"],
"run":["run","run","courir"],
"saw":["sawn / sawed","sawn / sawed","scier"],
"say":["said","said","dire"],
"see":["seen","seen","voir"],
"seek":["sought","sought","chercher"],
"sell":["sold","sold","vendre"],
"send":["sent","sent","envoyer"],
"set":["set","set","fixer"],
"shake":["shaken","shaken","secouer"],
"shed":["shed","shed","répandre / laisser tomber"],
"shine":["shone","shone","briller"],
"shoe":["shod","shod","chausser"],
"shoot":["shot","shot","tirer / fusiller"],
"show":["shown","shown","montrer"],
"shut":["shut","shut","fermer"],
"sing":["sung","sung","chanter"],
"sink":["sunk / sunken","sunk / sunken","couler"],
"sit":["sat","sat","s'asseoir"],
"slay":["slain","slain","tuer"],
"sleep":["slept","slept","dormir"],
"slide":["slid","slid","glisser"],
"slink":["slunk / slinked","slunk / slinked","s'en aller furtivement"],
"slit":["slit","slit","fendre"],
"smell":["smelt","smelt","sentir"],
"sow":["sown / sowed","sown / sowed","semer"],
"speak":["spoken","spoken","parler"],
"speed":["sped","sped","aller vite"],
"spell":["spelt","spelt","épeler / orthographier"],
"spend":["spent","spent","dépenser / passer du temps"],
"spill":["spilt / spilled","spilt / spilled","renverser"],
"spin":["spun","spun","tourner / faire tourner"],
"spit":["spat / spit","spat / spit","cracher"],
"split":["split","split","fendre"],
"spoil":["spoilt","spoilt","gâcher / gâter"],
"spread":["spread","spread","répandre"],
"spring":["sprung","sprung","surgir / jaillir / bondir"],
"stand":["stood","stood","être debout"],
"steal":["stolen","stolen","voler / dérober"],
"stick":["stuck","stuck","coller"],
"sting":["stung","stung","piquer"],
"stink":["stunk","stunk","puer"],
"strew":["strewn / strewed","strewn / strewed","éparpiller"],
"strike":["stricken / struck","stricken / struck","frapper"],
"strive":["striven","striven","s'efforcer"],
"swear":["sworn","sworn","jurer"],
"sweat":["sweat / sweated","sweat / sweated","suer"],
"sweep":["swept","swept","balayer"],
"swell":["swollen / swelled","swollen / swelled","gonfler / enfler"],
"swim":["swum","swum","nager"],
"swing":["swung","swung","se balancer"],
"take":["taken","taken","prendre"],
"teach":["taught","taught","enseigner"],
"tear":["torn","torn","déchirer"],
"tell":["told","told","dire / raconter"],
"think":["thought","thought","penser"],
"thrive":["thriven / thrived","thriven / thrived","prospérer"],
"throw":["thrown","thrown","jeter"],
"thrust":["thrust","thrust","enfoncer"],
"tread":["trodden","trodden","piétiner quelque chose"],
"typeset":["typeset","typeset","composer"],
"undergo":["undergone","undergone","subir"],
"understand":["understood","understood","comprendre"],
"wake":["woken","woken","réveiller"],
"wear":["worn","worn","porter (avoir sur soi)"],
"weep":["wept","wept","pleurer"],
"wet":["wet / wetted","wet / wetted","mouiller"],
"win":["won","won","gagner"],
"wind":["wound","wound","enrouler / remonter"],
"withdraw":["withdrawn","withdrawn","se retirer"],
"wring":["wrung","wrung","tordre"],
"write":["written","written","écrire"],
}
rand = random.choice(verbes.items())
verb, (pret, past, trad) = rand
# print "Le verbe %s se conjugue au prétérit par %s, au participe passé par %s et se traduit par %s" % (verb, pret, past, trad)
lst = []
lst.append(verb)
lst.append(pret)
lst.append(past)
lst.append(trad)
x = random.randint(0,3)
print "Le jeu consiste à trouver le verbe irrégulier, son prétérit et son participe passé, en fonction de sa traduction Française"
print "Par exemple : si le verbe '%s' est proposé, il faudra répondre '%s', '%s' et '%s'" % (lst[3], lst[0], lst[1], lst[2])

while counter < 10 :
    rand = random.choice(verbes.items())
    verb, (pret, past, trad) = rand
    # print "Le verbe %s se conjugue au prétérit par %s, au participe passé par %s et se traduit par %s" % (verb, pret, past, trad)
    lst = []
    lst.append(verb)
    lst.append(pret)
    lst.append(past)
    lst.append(trad)
    x = random.randint(0,3)
    print "Le jeu consiste à trouver le verbe irrégulier, son prétérit et son participe passé, en fonction de sa traduction Française"
    if x == 0:
        print "C'est le verbe à l'infinitif qui sort %s" % lst[0]
    elif x == 1:
        print "C'est le verbe au prétérit qui sort %s" % lst[1]
    elif x == 2:
        print "C'est le verbe au past qui sort %s" % lst[2]
    else:
        print "C'est la traduction du verbe qui sort %s" % lst[3]
        
    # print "Qu'est-ce qui va sortir %s" % lst[x]
    counter = counter + 1 

