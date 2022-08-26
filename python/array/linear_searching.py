#searching an array for an element
from array import *

arr = array('i', [])

n = int(input("Enter the size of the array: "))

print('Enter the element of the array: ')
for i in range(n):
    arr.append(int(input()))

print('Created array is: ', arr)

print('Enter element to search: ')
s = int(input())       #accepting element to be searched

#linear search
flag = False

for i in range(len(arr)):
    if s == arr[i]:
        print('Found at position:', i+1)
        flag = True

if flag == False:
    print('Not found in the array')