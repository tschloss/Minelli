#!/usr/bin/env python 
# coding: utf-8
input = '''Ha P W T&R
1304 1201 0100 1000 2431
0413 3001 0100 0010 2431
0017 0040 1000 1000 1342
0107 2011 0001 0100 4231
4004 0220 0001 0010 4321
0035 4000 1000 0100 4213
0314 1201 0001 0001 3412
3005 0130 0001 0010 1234
2033 0202 0001 1000 2341
4310 1021 0100 0100 3421''' 

rounds = input.split('\n')
moneybalance = [0,0,0,0]
chipbalance = [0,0,0,0]
htmlboard = '</table></html>'
	
def evaluate(game,type):
	global htmlboard
	gameresult = []
	for c in game:
		gameresult.append(int(c)) 
			
	if (type in (2,3)): factor = -8
	elif type == 1: factor = -2 
	elif type == 0: factor = -1
	else: factor = 0 
		
	if (type == 4):
		for i in range(len(gameresult)):
			if gameresult[i] == 1: gameresult[i] = 18
			elif gameresult[i] == 2: gameresult[i] = 10
			elif gameresult[i] == 3: gameresult[i] = 4
			else: gameresult[i] = 0 
				
	else: 
		for i in range(len(gameresult)):
			gameresult[i] *= factor
			
	chips = []
	for player in gameresult:
		balance = 0 
		for oponent in gameresult:
			if player > oponent: balance += 1
			elif player < oponent: balance += -1 			
		chips.append(balance)
				
	checksum = 0
	eurobalance=[]
	for i in range(len(gameresult)):
		moneybalance[i] += gameresult[i]
		chipbalance[i] += chips[i]
		eurobalance.append(moneybalance[i] + 2 * chipbalance[i])
		checksum += gameresult[i] 
			
	if (type==4 and checksum!=32) or (type in (0,1,2,3) and checksum!=-8) or not (type in range(5)): print("**ERROR**")
	
	#print (htmlboard)
	#htmlboard = htmlboard + 'x'
	htmlboard = '<tr><td>'+str(type+1)+'</td><td>'+game+'</td><td>'+str(moneybalance[0])+'</td><td>'+str(moneybalance[1])+'</td><td>'+str(moneybalance[2])+'</td><td>'+str(moneybalance[3])+'</td></tr>' + htmlboard
	
	resultstr = '{0:3d}|{1:3d}|{2:3d}|{3:3d}'.format(moneybalance[0], moneybalance[1],moneybalance[2],moneybalance[3])
	resultstr = resultstr + '   ({0:2d}|{1:2d}|{2:2d}|{3:2d}) '.format(gameresult[0], gameresult[1],gameresult[2],gameresult[3])
	resultstr = resultstr + '   {0:3d}|{1:3d}|{2:3d}|{3:3d} '.format(chipbalance[0], chipbalance[1],chipbalance[2],chipbalance[3])
	resultstr = resultstr + '  {0:3d}|{1:3d}|{2:3d}|{3:3d} '.format(eurobalance[0], eurobalance[1],eurobalance[2],eurobalance[3])
	return (resultstr) 
	#(str(gameresult) + ">" + str(moneybalance) + "|" + str(chips) + ">" + str(chipbalance) + "€" + str(eurobalance))


for roundidx,round in enumerate(rounds):
	games = round.split(' ')
	
	if roundidx>0 and len(games)>0:
		print (rounds[0] + "        PUNKTE TOT.        Punkte           Chips-tot          € tot.")
		for idx,game in enumerate(games):
			dealer = 1 + (roundidx*5+idx-1) % 4
			resultstring = evaluate(game,idx)
			print("S%2d/%1d[%1d]: %4s %s" % (roundidx,idx+1,dealer, game,resultstring))
			if idx==4: print()
			
#htmlboard = 'Spielstand:<table><th><td>1</td><td>2</td><td><td>3</td><td>4</td></th><tr><td>'+str(moneybalance[0])+'</td><td>'+str(moneybalance[1])+'</td><td>'+str(moneybalance[2])+'</td><td>'+str(moneybalance[3])+'</td></tr>'
htmlboard= '<table border="1"><tr><th align="center">Art</th><th align="center">Ergebnis</th><th>1</th><th>2</th><th>3</th><th>4</th></tr>' + htmlboard
htmlboard = '<html><body><style>td {border: 1px solid; padding: 8px; text-align: right;} body {width: 100%; }</style>' + htmlboard

import requests
url = 'http://net-hitec.de/mvonline/minelliupload.php'
files = {'userfile': ('minelli.html', htmlboard)}
r = requests.post(url, files=files)
print (r.text)
