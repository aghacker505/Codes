from array import *

a = array("i", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
#      index --- 0   1   2   3   4   5   6   7   8   9             
# n = len(a)
# print(n)

# arrayname[start:stop:stride]

#create array y with elements from 1st to 3rd index form a
y = a[1:4]    #here we write 4 but it include elements till 3rd index
print(y)


#create array y with elements from 0th to 3rd form a
y = a[0:4]
# y = a[:4]   #both are same
print(y)


#create array y with last 4 elements from x
y = a[-4:]
print(y)

#create array y with last 2 elements from x
y = a[-2:]
print(y)

#create array y with last 5th element with [-5-(-3) = -2] .i.e 2 elements 
#towards right
y = a[-5:-3]
print(y)


#create array y wiht 0th to 10th elements from x
# stride 2 means, after 0th element, retrieve every 2nd element from x
y = a[0:10:2]
print(y)