def index():
	try:
		gid = request.args[0]
	except IndexError:
		redirect(URL('game','index'))
	game = db(db.games.id == gid).select(db.games.name)[0]
	gname = game.name
	rows = db(db.groups.game == request.args[0]).select()
	return locals()

def add():
	try:
		i = request.args[0]
	except IndexError:
		redirect(URL('game','index'))
	form = crud.create(db.groups)
	form.vars.game = i
	if form.process().accepted:
		redirect(URL('index', args=[request.args[0]]))
	return locals()

def edit():
	try:
		request.args[0]
	except IndexError:
		redirect(URL('game','index'))
	form=crud.update(db.groups, request.args(0))
	if form.process().accepted:
		redirect(URL('index', args=[request.args[0]]))
	return locals()

def delete():
	try:
		request.args[0]
	except IndexError:
		redirect(URL('game','index'))
	db(db.groups.id == request.args(0)).delete()
	redirect(URL('index', args=[request.args[0]]))
	return locals()