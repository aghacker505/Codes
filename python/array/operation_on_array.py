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

#this will extend the array
ar1 = array('i', [60, 70, 80, 90, 100]) 
ar.extend(ar1)
print("here is the extended array: ", ar)

print("------------------------------------------------------------------------------")

#this will insert 25 at the 1st position 
ar.insert(1, 25)
print("This is array after insertion 25 at the first position",ar)

print('-----------------------------------------------------------------------------------')

#this will remove the elements from the array
ar.remove(30)  #this will remove the only first occurence of 30   
# ar.remove(30)  #this will remove the second occurence of 30   
print("This is the array after removing 30: ", ar)

print('----------------------------------------------------------------------------------')

#remove last element of ethe array using pop() method
p = ar.pop()
print("Array element poped/removed: ",p)
print("Array after removing poped element:", ar)

print('---------------------------------------------------------------------------')

#this will print the index of the elements of the array
d = ar.index(30)
print("The first occurence of the 30 the following array: ", d)

print("----------------------------------------------------------------")

#convert array into list using tolist() method
list = ar.tolist()
print("list: ", list)
print("array: ", ar)
