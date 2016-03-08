import numpy
import matplotlib
import matplotlib.pyplot
#objetivo: determinar la concentracion al cabo de 10 horas y graficar Q
#en funcion del tiempo con el algoritmo runge-kutta
#Estrategia:
k=0.2
Q0=200
delta=0.1

t=range(101)
l=range(101)

def f(n):
	return -k * n
for i in range(101):
	Q1=Q0+delta*f(Q0+0.5*delta*f(Q0))
	Q0=Q1
	t[i]=Q1*delta

print Q1

tnew=numpy.array(t)
lnew=numpy.array(l)
print lnew
print tnew
matplotlib.pyplot.plot(tnew,lnew)
matplotlib.pyplot.show()
print "la concentracion despues de 10 horas es:"
print t[100]
	




	








































