import numpy
import matplotlib
import matplotlib.pyplot
#objetivo: determinar la concentracion al cabo de 10 horas y graficar Q
#en funcion del tiempo
#Estrategia:
k=0.2
Q0=200
delta=0.1
t=range(101)
l=range(101)
for i in range(101):
	Q1=Q0-k*delta*Q0
	Q0=Q1
	l[i]=Q1
	t[i]=(i*0.1)
print l
tnew=numpy.array(t)
lnew=numpy.array(l)
print lnew
print tnew
matplotlib.pyplot.plot(tnew,lnew)
matplotlib.pyplot.show()
print "la concentracion despues de 10 horas es:"
print l[100]

	
