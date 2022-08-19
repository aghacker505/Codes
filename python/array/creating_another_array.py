#here we create can array with the help of another array
from array import *

arr1= array('d' , [10.5, 20.5, -4.5, 0.6])

# arr2 = array(arr1.typecode, [a for a in arr1])
arr2 = array(arr1.typecode, [a*2 for a in arr1])      #here we can also apply condition so value obtained from arr1 is multiplied by 2 
print("elements in the second array: ")

for i in arr2:
    print(i)
    