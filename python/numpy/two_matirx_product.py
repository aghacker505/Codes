import sys
from tkinter import Y
from numpy import *

#accept number of rows and cols of first matric into r1, c1
r1,c1 = [int(a) for a in input("First Matrix rows, cols: ").split()]

#accept number of rows and cols of Second matric into r1, c1
r2,c2 = [int(a) for a in input("Second Matrix rows, cols: ").split()]

#test the condition if c1 != r2, then multiplication is not possible 
if c1 != r2:
    print('Multiplication is not possible')
    sys.exit()   #terminate the program

# accept first matrix element as a string into str1
str1 = input('Enter the first matrix element:\n ')

# convert str1 into a matrix with size r1xc1
x = reshape(matrix(str1), (r1, c1))

# accept second matrix elements as a sting into str2
str2 = input('Enter second matrix elements:\n ')

# convert str2 into a matrix with size r2xc2
y = reshape(matrix(str2), (r2, c2))

print('The product matrix: ')
z = x*y
print(z)