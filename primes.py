#esta funcion calcula el numero minimo
def minimo(x,y):
	if x<y:
		return x
	else:
		return y
#esta funcion calcula el maximo comun divisor de dos numeros
def mcd(x,y):
	m=minimo(x,y)
	for i in range(m,0,-1):
		if x%i==0 and y%i==0:
			return i
#Esta funcion calcula si dos numeros son coprimos
def arecoprime(a,b):
	m=mcd(a,b)
	if m==1:
		return 1
	else:
		return 0
print arecoprime(16,7)
