def CreateEventData(x, y):
	z = dict()
	for i in x:
		if i in y:
			z[i] = y[i]
#		else:
#			z[i] = None
	return z
