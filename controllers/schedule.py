# -*- coding: utf-8 -*-
# try something like
from datetime import datetime, timedelta

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
	if request.vars.time:
		gtime = int(request.vars.time)
	else:
		gtime = 0
	if request.vars.gskip:
		gskip = int(request.vars.gskip)
	else:
		gskip = 0
	if request.vars.glen:
		glen = str(request.vars.glen)
	else:
		glen = 60
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

	#parsing input
	if request.vars.gdata:
		data = request.vars.gdata
		if len(data) == 0:
			data = "False"
	else:
		data = "False"

	slots = []
	error = []
	if data != "False":
		arr = data.split('\r\n')
		i = 0
		for row in arr:
			if row == "":
				continue
			i += 1
			values = row.split(',')
			if len(values) != 4:
				error.append('Wrong number of arguments at line ' + str(i))
				continue
			st = values[2].split(':')
			if len(st) !=2:
				error.append('Wrong format for start time at line ' + str(i))
				continue
			et = values[3].split(':')
			if len(et) !=2:
				error.append('Wrong format for end time at line ' + str(i))
				continue

			#time divisions
			start = datetime.now().replace(hour=int(st[0]), minute=int(st[1]))
			end = start + timedelta(minutes = int(glen))
			dend = datetime.now().replace(hour=int(et[0]), minute=int(et[1]))
			while end <= dend:
				slots.append([values[0], values[1], start.strftime("%H:%M") , end.strftime("%H:%M")])
				start = end + timedelta(minutes = int(gskip))
				end = start + timedelta(minutes = int(glen))
	else:
		arr = 0
	err = 0
	if len(slots) == 0 and gtime == 1:
		gtime = 0
		err = 1
		error.append('Invalid Game Data Input')

	return locals()