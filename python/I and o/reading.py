#use open function to read the content of the file!

# f = open('main.txt', 'r')  #open function
f = open('main.txt')  #by defalut the mode is r .i.e reading mode
# data = f.read()   #read function/read its content
data = f.read(10)  #if we enter value in the bracket............so it will read only first 10 character of the file
print(data) #print its content
f.close()  #close the file

#we use w to write in file