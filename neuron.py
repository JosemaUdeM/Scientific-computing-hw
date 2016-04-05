import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import math 
from scipy.interpolate import interp1d

x= np.linspace (0,5,num=10, endpoint=True)
y= np.cos(-x**2 / 9.0)
f= interp1d(x,y,kind = 'cubic')

Delta=0.001
delta=0.003
CM=1
I=15

Vk=-12
ki=150
ko=5.5
VNa=115
Nai=15
Nao=150
VL=10.599
gK=36
gNa=120
gL=0.3

T=6.3



def phi(T): 
	return 3**((T-6.3)/10)



def an(V):
	return phi(T)*(0.01*(10-V)/(math.exp((10-V)/10)-1))
	
def Bn(V):
	return phi(T)*(0.125 *math.exp(-V/80))


def am(V):
	return phi(T)*(0.01*(25-V)/(math.exp((25-V)/10)-1))
	
def Bm(V):
	return phi(T)*4*math.exp(-V/18)

	
def ah(V):
	return phi(T)*0.07*math.exp(-V/20)

def Bh(V):
	return phi(T)*1/(math.exp((30-V)/10)+1)

def IK(V,n): 
	return gK*n**4*(V-Vk)

def IL(V): 
	return gL*(V-VL)
def INa(V, m, h): 
	return gNa*m**3*h*(V-VNa)


def fp(V, n, m, h): 
	Vdt = (I-IK(V, n)-INa(V, m, h) -IL(V))/CM
	ndt = an(V)*(1-n) -Bn(V)*n
	mdt = am(V)*(1-m) - Bm(V)*m
	hdt = ah(V)*(1-h) -Bh(V)*h
	return Vdt, ndt, mdt, hdt 


t = np.linspace(0, 5, num =20000, endpoint=True)
n = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))
V = np.zeros(len(t))

V[0]=-65
n[0]=0.317
m[0]=0.05
h[0]=0.6

for i in range(len(t)-1):

   Vdt, ndt, mdt, hdt = fp(V[i], n[i], m[i], h[i])

   Vdtt, ndtt, mdtt, hdtt = fp(V[i] + (0.5*delta*Vdt), n[i] + (0.5*delta*ndt), m[i] + (0.5*delta*mdt), h[i] + (0.5*delta*hdt))
   V[i+1] = V[i] + (delta*Vdtt)	
   n[i+1] = n[i] + (delta*ndtt)
   m[i+1] = m[i] + (delta*mdtt)
   h[i+1] = h[i] + (delta*hdtt)

										

## Graphics
plt.plot(t, m, 'r', label='m')
plt.plot(t, h, 'g', label='h')
plt.plot(t, n, 'b', label='n')
plt.legend()
plt.show()

plt.plot(V,n)
plt.title('Phase space Voltage vs n')
plt.show()

plt.plot(t,V)
plt.xlabel('t')
plt.ylabel('V(t)')
plt.show() 
