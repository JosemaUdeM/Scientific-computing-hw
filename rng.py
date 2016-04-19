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
	
	t=200

	xn = np.random.normal (0,1,n)
	xn [0]=0
	bins=50
	y1,x1 = np.histogram(xn,bins = bins, density = True)
	x1= x1 [0 : -1] + 0.5 * (x1[1] - x1[0])
	plt.plot (x1,y1, 'b-')
	plt.show()

print brownian(200)
		
		

