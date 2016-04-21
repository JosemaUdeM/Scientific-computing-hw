import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#np.random.seed(0)

#n=50000
#xu = np.random.uniform(-20,20,n)
#xb = np.random.binomial(200,0.25,n)
#xn = np.random.normal (0.0,10,n)


#bins = 30

#y1, x1 = np.histogram(xu,bins = bins, density = True)
#y2, x2 = np.histogram(xb,bins = bins, density = True)
#y3, x3 = np.histogram(xn,bins = bins, density = True)

#x1= x1 [0 : -1] + 0.5 * (x1[1] - x1[0])
#x2= x2 [0 : -1] + 0.5 * (x2[1] - x2[0])
#x3= x3 [0 : -1] + 0.5 * (x3[1] - x3[0])

#plt.plot (x1,y1, 'b-')

#plt.plot (x2,y2, 'r-')

#plt.plot (x3,y3, 'g-')
#plt.show()




def brownian(n):
	x = np.random.normal(0.0,1, n)
	x[0] = 0
	x1= np.cumsum(x)
	return x1
plt.plot(brownian(200))
plt.show()

def brownian2D(n, delta):
	return brownian(n, delta), brownian(n, delta)
	x, y = brownian2D(200, 0.2)
plt.plot(x,y,'-')
plt.plot(x[0], y[0], 'go')
plt.plot(x[-1], y[-1], 'ro')
plt.show()


