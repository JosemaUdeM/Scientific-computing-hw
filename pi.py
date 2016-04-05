import numpy as np
import math


L=3.0
R=1.0
N=1000


def pi(L, R, N): 
 	n=0.0
	for i in range(N):
		x=L/2-L*np.random.random()
		y=L/2-L*np.random.random()
		Puntoxy=np.sqrt(x**2+y**2 )
		if Puntoxy<=R : 
			n=n+1
	return (n/N)*(L/R)**2

print "Numero pi aproximado:", pi(L,R,N)
