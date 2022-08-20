#accessing the elements of array using index

from array import *

roll_no = array('i' , [2, 16, 45, 46])

n = len(roll_no)  #this will find the number of array

print(n)  #this will print the number of array

#this will display number of elements using indexing
for i in range(n):
    print(roll_no[i], end= ' ')

#this whole process is called indexing