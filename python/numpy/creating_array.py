# import numpy 
# import numpy as np
from numpy import *

# array_name = array([array_elements], datatype)
ar = array([10, 20, 30, 40 ,50], int)
# ar = array([10, 20, 30, 40 ,50)
#we can eleminate 'int' from the above array since python automatically identify datatype of the integer

ar1 = array([1.2, 12.5, -6.5, 6.8, 5.6], float)
ar1 = array([1.2, 12.5, -6.5, 6.8, 5.6])
#we can also eleminate 'float' from the above array since python also identify datatype of the float
#if pythn interpreter finds one element belonging to 'float type', then it will convert all the other element
#also into float type by adding decimal point after the element
ar2 = array([10, 20, 30, 40.2, 50])

print(ar)
print(ar1)
print(ar2)

#similarly for the character type elements, we need not specify the datatype of the array