# with open('write.txt', 'r') as f:
#     a = f.read()

# with open('write.txt', 'w') as f:
#     a = f.write("Python is very simple language")

with open('write.txt', 'a') as f:
    a = f.write("\nit is easy to learn")
print(a)


#best way to open and close the file