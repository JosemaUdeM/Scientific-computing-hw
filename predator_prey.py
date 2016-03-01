#marzo 1,2016
#Tema:lokta-volterra model
#objetivo: determinar la interaccion de 2 especies (predador y presa)
#siendo delta la funcion del tiempo con respecto a x depredador y y #presa
import numpy
import matplotlib
import matplotlib.pyplot
delta = 0.1
x0=15
y0=100
ky=2.0
kyx=0.01
kxy=0.01
kx=1.06
t=range(11)
l=range(11)
for i in range(11):
	y1=y0+delta*ky*y0-kxy*x0*y0
	x1=x0+delta*kyx*y0*x0-kx*x0
	y0=y1
	x0=x1
	t[i]=y1
for r in range(11):
	y1=y0+delta*ky*y0-kxy*x0*y0
	x1=x0+delta*kyx*y0*x0-kx*x0
	y0=y1
	x0=x1
	l[i]=x1

print t
print l
tnew=numpy.array(t)
lnew=numpy.array(l)
print tnew
print lnew

matplotlib.pyplot.plot(tnew,lnew)
matplotlib.pyplot.show()
