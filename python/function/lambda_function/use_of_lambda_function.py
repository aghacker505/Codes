a = [22, 29 , 30, 31, 32, 33, 34, 35, 36]

#filter function
#this is the function that will extract the even values from the list
final_list = list(filter(lambda x: (x%2 == 0), a))
print(final_list)

#map funtion along wiht lambda function
#here this function will multiply all the values in the list with 10
final_list = list(map(lambda x: (x*10), a))
print(final_list)

#reduce function
from functools import reduce

sum = reduce((lambda x,y: x + y), a)
print("reuced function is",  sum) 