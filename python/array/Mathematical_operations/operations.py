#mathematical operations on arrays

from numpy import *

arr = ([10, 30, 20.15, -40])
print("Original array: ", arr)

# do arithmetic operations on the elements of the array
# print("After adding 5: ", arr+5)
# print("After subtracting 5: ", arr-5)
# print("After dividing with 5: ", arr/5)
# print("After multiplication with 5: ", arr*5)
# print("After modulus with 5: ", arr*5)

#we can also use the array in expressions also
# print("Expression value: ",(arr+5)**2-10)

# do some math function
print("Sin values: ", sin(arr))
print("Cos values: ", cos(arr))
print("tan values: ", tan(arr))
print("Biggest element: ", max(arr))
print("Smallest elements: ", min(arr))
print("Sum of all elements: ", sum(arr))
print("Average of all elements: ", mean(arr))
print("Sorted array: ", sort(arr))