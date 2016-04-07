import numpy as np

N=(input('ingrese el valor de veces que quiere lanzar la moneda:'))
L=N
def rwalk1d(N):
	for i in range(N):
		posicion=0
		
		x=L/2-L*np.random.random()
	
		if x < 0:
			posicion=posicion-1
		else:
			if x > 0:
				posicion=posicion+1
		return posicion
	
print 'la posicion final despues de', N ,'iteracciones es:',rwalk1d(N)
