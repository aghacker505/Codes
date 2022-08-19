#read first line only
f = open('main.txt')
data = f.readline()

#read second line only
print(data) 
data = f.readline() 

#read third line only
print(data) 
data = f.readline() 
print(data) 

#read fourth line only and so on..... 
data = f.readline() 
print(data) 

f.close()  

#read line will print the content of the text line by line with next line .i.e \n command