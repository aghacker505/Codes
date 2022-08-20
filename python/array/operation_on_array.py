#operation onn arrays

from array import *

ar = array('i', [10, 20, 30, 40, 50])
print("original array: ", ar)

print("-----------------------------------------------------------------------")

#this will add elements in the end of the arrays
ar.append(30)
ar.append(100)
print('After append the new array is: ', ar )

print("-------------------------------------------------------------------------")

#this will give the occurences of 30 in the array
o = ar.count(30)
print("Number of occurences of 30 in the array: ", o)       

print("-------------------------------------------------------------------------")

ar1 = array('i', [60, 70, 80, 90, 100]) 
ar.extend(ar1)
print("here is the extended array: ", ar)