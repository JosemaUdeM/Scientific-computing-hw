import numpy as np
import matplotlib
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, num=1000)

def cost(x):
	
	return (np.exp(-(x-1)**2)*np.sin(8*x)+1)

plt.plot(x,cost(x))
plt.show()


#def neighbor(x)
#	step_size=1.0
#	return (2*np.random.random()-1)*
	
