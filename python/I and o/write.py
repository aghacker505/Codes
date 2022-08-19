#here write function will write the text you enter in the file
#it will automatically create the file if it is not exist
#if we run this programm it will overwrite the text writen in the file 

A = open('write.txt', 'w')  #w used for write the function
A.write("write this text in the file \n")                #if we write this function miltiple time it will write the text multiple times
A.write("write this text in the file \n")
A.write("write this text in the file")
A.close()


A = open('write.txt', 'a')  #a used for append the function
A.write("\n this line will append in the file")    #this will add the text in file      #as many time we run this command lines will add        
A.close()