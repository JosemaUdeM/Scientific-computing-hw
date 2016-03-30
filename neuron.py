import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys


x= np.linspace (0,10,num=10, endpoint=True)
y= np.cos(-x**2 / 9.0)
f= interp1d (x,y,kind = 'cubic')

Delta=0.001
CM=0.5
I=15
V=-65
Vk=-77
ki=150
ko=5.5
VNa=50
Nai=15
Nao=150
VL=-54.4
gK=36
gNa=120
gL=0.3
n=0.317
m=0.05
h=0.6
T=6.3
phi=3**((T-6.3)/10)



ah=phi*(0.07 np.exp(V/20))
	
	

Bn=phi*(0.125 np.exp(V/80))
	

Bm=phi*(4 np.exp(V/18))
	


an=phi*(0.01*(V+10)/(np.exp((V+10)/10)-1))
	

am=phi*(0.01*(V+25)/(np.exp((V+25)/10)-1))
	


Bh=phi*(1/(np.exp((V+30)/10)+1))
	
for i in range(0,6)
	n1= n+delta*(an*(1-n)-Bn*n)
	n=n1
for t in range(0,6)
	m1= m+delta*(am*(1-m)-Bm*m)
	m=m1
for l in range(0,6)
	h1= h+delta*(ah*(1-h)-Bh*h)
	h=h1
