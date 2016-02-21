# -*- coding: utf-8 -*-
# try something like
def index():
	games = db(db.games.id > 0).select()
	return locals()

def game(): 
	if(request.vars.game):
		gameId = int(request.vars.game)
	else:
		redirect(URL('index'))
	row = db.games(gameId)
	game = row.name
	pitch = row.pitch
	return locals()

def league():
	if(request.vars.arenas):
		arenas = int(request.vars.arenas)
	else:
		arenas = 1
	if request.vars.number > 1:
		num = int(request.vars.number)
	else:
		redirect(URL('index'))
	if(request.vars.practice):
		practice = True
	else:
		practice = False
	if(request.vars.game):
		gameId = int(request.vars.game)
	else:
		redirect(URL('index'))
	if request.vars.custom:
		custom = int(request.vars.custom)
		it = request.vars.it
	else:
		custom=0
	z=request.vars.copy()
	home = z.copy()
	home['custom']=0
	row = db.games(gameId)
	game = row.name
	pitch = row.pitch
	city = request.vars.city

	rotation = ["Team" + str(i+1) for i in range(num)]

	if num % 2:
		rotation.append('BYE')
		num += 1

	fixtures = []
	for i in range(0, num-1):
		fixtures.append(rotation)
		rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
	matches = []
	for f in fixtures:    
		for i in range(len(f)/2):
			if "BYE" not in (f[i], f[num-i-1]):
				if practice:
					matches.append(tuple((f[i], "Practice")))
					matches.append(tuple((f[num-i-1], "Practice")))
				matches.append(tuple((f[i], f[num-i-1])))
	return locals()