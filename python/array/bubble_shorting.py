from array import *

a = array('i', [])

n = int(input("Enter the size of the array: ")) 
# print("Enter the size of the array: ")
# n = int(input())

for i in range(n):
    print("Enter the elements: ")
    a.append(int(input()))      #here we use int because we enter intger elements but it accept the elements in the form of string 

print("original array: ", a)

# bubble shorting
swapped= False
for i in range(n-1):      # i is from 0 to n-1
    for j in range(n-1-i):    #j is from 0 to one element lesser than i
        if a[j] > a[j+1]:     #if 1st elemenst is bigger than the 2nd one
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
            swapped = True

    if swapped == False:
        break
    else:
        swapped = False

print("shorted array = ", a)