from array import *

marks = array('i', [95, 96, 90, 98, 80])

n = len(marks)
print(n)  #print the number of elements

i= 0
print("Marks are ")
while i<n:
    print(marks[i], end ="\n" )
    i+=1