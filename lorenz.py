#clase del 3 de marzo
import numpy
import matplotlib
import matplotlib.pyplot

sigma=10
beta=2.667
rho=28
delta=0.01
x0=0
y0=1
z0=1.05

t=range(101)
x=range(101)
z=range(101)
y=range(101)
y[0]=y0
x[0]=x0
z[0]=z0
for i in range(101):
	x1=delta*(sigma*(y0-x0))
	y1=delta*(x0*(rho-z0)-y0)
	z1=delta*((x0*y0)-(beta*z0))
	x0=x1
	y0=y1
	z0=z1
	x[i]=x1
	y[i]=y1
	z[i]=z1
	t[i]=i*delta

ynew = numpy.array(y)
xnew = numpy.array(x)
tnew = numpy.array(t)
znew = numpy.array(z)
print ynew
print xnew
print znew
print tnew
matplotlib.pyplot.plot(xnew,znew)
matplotlib.pyplot.plot(znew,xnew)
matplotlib.pyplot.show()




	

