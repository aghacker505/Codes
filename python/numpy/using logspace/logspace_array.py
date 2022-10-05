#logspace(start, stop, n)
#starts at the value which is 10 to the power of 'start'
#stop at the value which is 10 to the power of 'stop'

from numpy import *

a = logspace(1, 4, 5)
print(a)

n = len(a)
#repeat from 0 to n-1 times
for i in range(n):
    print('%.1f' % a[i], end=', ')