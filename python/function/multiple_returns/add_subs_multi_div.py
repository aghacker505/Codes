def num(a, b):
    ''' this function will return the result of
    addition, substraction, multiplication and division'''
    c = a+b 
    d = a-b 
    e = a/b 
    f = a*b

    return c,d,e,f


x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

res = num(x, y)
print("Sum, subs, divison and multi of the number you enter are respectivily: ")

for i in res:
    print(i)
    print(i, end = " ")  #using end we can define where to print the results or output