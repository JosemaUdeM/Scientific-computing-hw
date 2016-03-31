import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math 
from scipy.interpolate import interp1d

x= np.linspace (0,10,num=10, endpoint=True)
y= np.cos(-x**2 / 9.0)
f= interp1d(x,y,kind = 'cubic')

Delta=0.001
delta=0.003
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
Q=range(0.0,0.6)
z=range(0,6)

phi=3*math.exp((T-6.3)/10)



ah=phi*(0.07 *math.exp(V/20))
	
	

Bn=phi*(0.125 *math.exp(V/80))
	

Bm=phi*(4 *math.exp(V/18))
	


an=phi*(0.01*(V+10)/(math.exp((V+10)/10)-1))
	

am=phi*(0.01*(V+25)/(math.exp((V+25)/10)-1))
	


Bh=phi*(1/(math.exp((V+30)/10)+1))
	
for i in range(0.0,0.6):
	n1= n+delta*(an*(1-n)-Bn*n)
	
	Q[i]=n1
	z[i]=i*delta
	n=n1
Qnew=np.array(Q)
znew=np.array(z)	
plt.plot(Qnew, znew)
plt.show()
												
for t in range(f(0),f(5)):
	m1= m+delta*(am*(1-m)-Bm*m)
	
	Q[t]=m1
	z[t]=t*delta
	m=m1

for l in range(f(0),f(5)):
	h1= h+delta*(ah*(1-h)-Bh*h)
	h=h1
	Q[l]=h1
	z[l]=l*delta
	h=h1

for w in range(f(0),f(5)):
	V1=V+delta*((I-gK*n1**4*(V-Vk)-gNa*m1**3*h1*(V-VNa)-gL*(V-VL))/CM)
	V=V1
	Q[w]=V1
	z[w]=W*delta



plt.plot(Q, z)
plt.show()



