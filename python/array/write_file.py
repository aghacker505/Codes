from array import *

#first we created two arrays
a = array('u', ['a', 'b', 'h', 'a', 'y' ])
a1 = array('u', ['g', 'u', 'p', 't', 'a'])

#then open our file in writing mode using wb mode
f = open('file1.txt', 'wb')

#here we convert our into file
a.tofile(f)
a1.tofile(f)

#file closed
f.close()

#again open file in reading mode for reading
f = open('file1.txt', 'r')

#read the file in text variable
text = f.read()

#print our file 
print(text)
f.close() #file close after reading
'''------------------------------------------------------------------------------'''