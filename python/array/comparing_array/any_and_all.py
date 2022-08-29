from numpy import *

a = array([10, 20, 30, 50, 40])
b = array([1, 20, 30, 40, 50])

c = a == b
print("Result of a==b: ", c)

print('Check if any one element is true: ', any(c))
print('Check if all element is true: ', all(c))