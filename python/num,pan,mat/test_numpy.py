import numpy as np

a = np.zeros(shape=(5,5))
a[2,2]=9
a[:,0]=1
a[:,4]=1

a[0,:]=1
a[4,:]=1
print(a)

b= np.array([[5,7,8],[8,9,0]])
print(b)