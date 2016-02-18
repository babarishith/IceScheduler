# -*- coding: utf-8 -*-
# try something like
def index(): 
	return dict(message="hello from schedule.py")

def league():
	if(request.vars.number):
		num = int(request.vars.number)
	else:
		redirect(URL('index'))
	if(request.vars.rinks):
		rinks = int(request.vars.rinks)
	else:
		rinks = 1
	if(request.vars.practice):
		practice = True
	else:
		practice = False
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