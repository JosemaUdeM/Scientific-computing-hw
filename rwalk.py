import numpy as np
import random



def rwalk1d(N,p):
	S=0
	for i in range(N):
		
		
		x=np.random.random()
		
		if x < p:
			S=S-1
		else:
			S=S+1
	return S
		
print 'la posicion final es:',rwalk1d(1000,0.69)
