from numpy import *

n1 =  array([10, 20, 30, 40, 50])
save('my_array', n1)
n2 = load('my_array.npy')
print(n2)