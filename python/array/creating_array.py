from array import *    

'''here '*' represents 'all' 
which means immport all (classes, objects, variable, etc) from the array module into our program'''

# import array  #this will immport only array module in our program

# import array as ar

arr = array('i', [2,4,6,8])
arr = array('d', [2.22,4.5,6,8])
arr = array('u', ['a','b','c','d'])

#in bottom two cases we have to mention module name
# arr = array.array('f', [2.22,4.5,6,8])  #for 6th line we have to mention the module name .i.e 'array'   
# arr = ar.array('d', [2.22,4.5,6,8])  #for 8th line  we have to mention module name .i.e 'ar'

print("the elements of array are: ")

for item in arr:
    print(item)

# print(arr) #this will print the array
'''
'i' for integers
'd' for doubles
'f' for floats
'u' for characters
'''