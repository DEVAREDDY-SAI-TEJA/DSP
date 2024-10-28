import numpy as np 
from matplotlib import pyplot as plt
def cyclicdelay(x,m):
    N=len(x)
    y=[]
    for n in range(0,N):
        if n-m >=0:
            idX=(n-m) % N
        else:
            idx=N+n-m
        y.append(x[idx])
    return y
a=[1,2,3,4,5]
b=3
print(cyclicdelay(a,b))