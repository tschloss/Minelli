#!/usr/bin/env python 
# coding: utf-8

input = '''Ha Ho&W M T&R 
0224 1102 0010 1000 1234
4004 1111 0100 0001 4231
2222 2200 0001 1000 3412
7010 2011 0100 0001 2431
1133''' 

rounds = input.split('\n')
moneybalance = [0,0,0,0]
chipbalance = [0,0,0,0]
	
def evaluate(game,type):
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
		
	return (str(gameresult) + ">" + str(moneybalance) + "|" + str(chips) + ">" + str(chipbalance) + "€" + str(eurobalance))
		
for roundidx,round in enumerate(rounds):
	games = round.split(' ')
	
	if roundidx>0 and len(games)>0:
		print (rounds[0] + "      €         €-total         Chips        Chips-tot        TOTAL")
		for idx,game in enumerate(games):
			resultstring = evaluate(game,idx)
			print("S%2d/%1d: %4s %s" % (roundidx,idx+1,game,resultstring))
			if idx==4: print()
