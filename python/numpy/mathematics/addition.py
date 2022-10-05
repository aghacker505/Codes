from numpy import *
n1 = array([10, 20, 30, 40, 50])
n2 = array([50, 60, 70, 80, 90])

print(sum([n1, n2])) #this will add all the elements of array n1 and n2 together
print(sum([n1, n2], axis=0))  #this will add all the elements of the n1 and n2 index wise
print(sum([n1, n2], axis=1)) #this will add all the elements of the n1 and n2 separately