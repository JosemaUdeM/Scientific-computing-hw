import numpy as np
import matplotlib
import matplotlib.pyplot as plt
n= 100
w = np.zeros ([n,n] , dtype = np.int8)

#0=east ; 1= south ; 2= west ; 3= north
#d = direccion
#c = color

east = 0
south = 1
west = 2
north = 3

d=0
c=0 
Blanco=0
Negro=1

i= n/2
j= n/2


def nextdirection (d,c):
	if  c== Blanco:
		if d== west:
			dfinal= north	
		if d== north:
			dfinal= east
		if d== south:
			dfinal= west
		if d== east:
			dfinal= south
	else:
		if d== west:
			dfinal= south
		if d== north:
			dfinal= west
		if d== south:
			dfinal= east
		if d== east:
			dfinal= north
	return dfinal
	

def moveforward (i,j,dfinal):
	w[i,j] = 1
	if d== west:
		w[i,j+1]=1
	if d== south:
		w[i+1,j]=1
	if d== east:
		w[i,j-1]=1
	if d== north:
		w[i-1,j]=1
	return w
	
#def validindex(i,j,n):

for i in range(200):
	x = [east, west, south, north]
	a = np.random.choice(x)
	y = [Negro, Blanco]
	b = np.random.choice(y)
	p = nextdirection(a,b)
	moveforward(n/2, n/2, p) 



	
	




plt.imshow(w, interpolation='none', cmap=plt.cm.Greys, extent=(0,n,0,n))
plt.show()


