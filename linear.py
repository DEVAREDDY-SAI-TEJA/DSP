import numpy as np
from matplotlib import pyplot as plt
x=np.array([1,2,33,43])
y=np.array([4,3,2,1])
s=(x+y)
#fouier transform
xf=np.fft.fft(x)
yf=np.fft.fft(y)
sf=np.fft.fft(s)
sumf=xf+yf
print(sumf)
print(sf)
a=np.allclose(sf,sumf)
print(a)
plt.subplot(2,1,1)
plt.plot(sf)
plt.subplot(2,1,2)
plt.plot(sumf)
plt.show()






