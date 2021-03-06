# -*- coding: utf-8 -*-
# try something like
def index():
	games = db(db.games.id > 0).select()
	return locals()

def edit():
	try:
		request.args[0]
	except IndexError:
		redirect(URL('index'))
	#form=crud.update(db.games, request.args(0))
	db.games.id.readable = False
	record = db.games(request.args[0])
	form = SQLFORM(db.games, record)
	if form.process().accepted:
		redirect(URL('index'))
	return locals()

def delete():
	try:
		request.args[0]
	except IndexError:
		redirect(URL('index'))
	db(db.games.id == request.args(0)).delete()
	redirect(URL('index'))
	return locals()

def add():
	#form=crud.create(db.games)
	form = SQLFORM(db.games)
	if form.process().accepted:
		redirect(URL('index'))
	return locals()
	