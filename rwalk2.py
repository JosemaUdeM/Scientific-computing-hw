import numpy as np
import random

N=2000		#N=pasos
B=range(100)  #B=Borrachos

def rwalk1d(N):
	S=0
	for i in range(N):
		h=1+(N/2-N*random.random())

		if h < 0:
			S=S-1
		else:
			if h > 0:
				S=S+1
			else:
				S=S
	return S
#print 'la posicion final es:',rwalk1d(1000,0.69)






def rw(B,N):
	c=0
	for i in range (100):
		x=rwalk1d(N)
		if x[i]==x[i]:
			c=c+1
			print c
	

print rw(B,N)		
	
	
	
