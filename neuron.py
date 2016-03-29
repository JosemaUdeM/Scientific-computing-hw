import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys


x= np.linspace (0,10,num=10, endpoint=True)
y= np.cos(-x**2 / 9.0)
f= interp1d (x,y,kind = 'cubic')

Delta=0.01
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
phi=3**(T-6.3)/10


def alfah(phi,V):
	ah=phi(0.07 np.exp(V/20))
	return ah
	
def Betan(phi,V)
	Bn=phi(0.125 np.exp(V/80))
	return Bn

def Betam(phi,V)
	Bm=phi(4 np.exp(V/18))
	return Bm


	
