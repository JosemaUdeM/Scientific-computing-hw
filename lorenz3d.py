#atractor de lorenz
#grafica 3D del atractor de lorenz
#creado por Jose Manuel Vergara
#7 de marzo,2016
#donde t = al tiempo, x = la conveccion del aire, y= que tanto sube y baja el aire, z = describe cuanto se desvia la temperatura :v
import numpy
import matplotlib
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')

sigma=10
beta=2.667
rho=28
delta=0.01
x0=0
y0=1
z0=1.05

t=range(10001)
x=range(10001)
z=range(10001)
y=range(10001)
y[0]=y0
x[0]=x0
z[0]=z0
for i in range(10001):
	x1=(delta*sigma*y0)-(delta*sigma*x0)+x0
	y1=(delta*x0*rho)-(delta*x0*z0)-(delta*y0)+y0
	z1=(delta*x0*y0)-(delta*beta*z0)+z0
	x0=x1
	y0=y1
	z0=z1
	x[i]=x1 
	y[i]=y1
	z[i]=z1
	t[i]=i*delta


ax.scatter(x,y,z)
ax.set_xlabel( ' x label')
ax.set_ylabel( ' y label')
ax.set_zlabel( ' z label')
plt.show()
