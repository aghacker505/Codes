from numpy import *
n1 = array([10, 20, 30, 40, 50])
n2 = array([50, 60, 70, 80, 90])

#join the array column wise
print(column_stack((n1, n2)))