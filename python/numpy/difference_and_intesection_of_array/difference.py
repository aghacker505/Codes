from numpy import *
n1 = array([10, 20, 30, 40, 50])
n2 = array([50, 60, 70, 80, 90])

print(setdiff1d(n1, n2))    #elements present in only n1 array or unique elements of the n1 array
print(setdiff1d(n2, n1))    #elements present in only n2 array or unique elements of the n2 array