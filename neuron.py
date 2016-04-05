import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math 
from scipy.interpolate import interp1d

delta=0.003
Delta=0.001

valnum=5/Delta
x= np.linspace (0,5,num=valnum, endpoint=True)
#y= np.cos(-x**2 / 9.0)
#f= interp1d (x,y,kind = 'cubic')





CM=0.5
I=15
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

T=6.3

Q=np.zeros(len(x))
Q1=np.zeros(len(x))
Q2=np.zeros(len(x))
Q3=np.zeros(len(x))

V=-65
n=0.317
m=0.05
h=0.6

def phi(T): 
	return 3**((T-6.3)/10)



def IK(n, V):
	iK = gK*(n**4)*(V-VK)
	return iK

def IL(V):
	iL = gL*(V-VL)
	return iL
def INa(m, h, V):
	iNa = gNa*(m**3)*h*(V-VNa)
	return iNa

def an(V):
	return phi(T)*(0.01*(10-V)/(math.exp((10-V)/10)-1))
	
def Bn(V):
	return phi(T)*(0.125 *math.exp(-V/80))


def am(V):
	return phi(T)*(0.01*(25-V)/(math.exp((25-V)/10)-1))
	
def Bm(V):
	return phi(T)*(4 *math.exp(-V/18))

	
def ah(V):
	return phi(T)*(0.07 *math.exp(-V/20))

def Bh(V):
	return phi(T)*(1/(math.exp((30-V)/10)+1))




def Funciones(n,m,h):
#	V1 = (I-IK(n, V)-INa(m, h, V)-IL(V))/CM
	n1 = an(V)*(1-n)-Bn(V)*n 
	m1 = am(V)*(1-m)-Bm(V)*m
	h1 = ah(V)*(1-h)-Bh(V)*h  
	return n1, m1, h1
	
for i in range (len(x)):

	N,M,H = Funciones (n,m,h)
	N1=n+delta*N
	M1=m+delta*M
	H1=h+delta*H
#	n1= n+delta*(an*(1-n)-Bn*n)
#	m1= m+delta*(am*(1-m)-Bm*m)
#	h1= h+delta*(ah*(1-h)-Bh*h)
	
	Q[i]=N1
	Q1[i]=M1
	Q2[i]=H1


	
	n=N1
	m=M1
	h=H1


	
plt.plot(x,Q)
plt.plot(x,Q1)
plt.plot(x,Q2)

plt.show()
