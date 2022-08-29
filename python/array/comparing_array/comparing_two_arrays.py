from numpy import *

a = array([10, 20, 30, 50, 40])
b = array([1, 20, 30, 40, 50])

c = a == b
print("Result of a==b: ", c)

c = a > b
print("Result of a>b: ", c)

c = a <= b
print("Result of a<=b: ", c)

c = a != b
print("Result of a!=b: ", c)

'''
these operators used in array compare the corresponding elements of the array
and return another with with Boolean type values
which means resuating array contain elements which are
True or False'''