
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
<<<<<<< HEAD
t=range(11)
l=range(11)
for i in range(11):
	y1=y0+delta*ky*y0-kxy*x0*y0
	x1=x0+delta*kyx*y0*x0-kx*x0
	y0=y1
	x0=x1
	t[i]=y1
	l[i]=x1

print t
print l

=======
y=range(101)
x=range(101)
t=range(101)
y[0]=y0
x[0]=x0
for i in range(101):
	y1=(delta*ky*y0)-(delta*kxy*x0*y0)+y0
	y0=y1
	x1=(delta*kyx*y0*x0)-(delta*kx*x0)+x0
	x0=x1
	y[i]=y1
	x[i]=x1
	t[i]=i*delta

print y
print x
ynew=numpy.array(y)
xnew=numpy.array(x)
>>>>>>> 4910235ab7141de1f548e79b418b498a3a75fbe5
tnew=numpy.array(t)
print ynew
print xnew

matplotlib.pyplot.plot(xnew,ynew)
matplotlib.pyplot.plot(ynew,xnew)
matplotlib.pyplot.show()
matplotlib.pyplot.plot(tnew,xnew)
matplotlib.pyplot.plot(tnew,ynew)
matplotlib.pyplot.show()
