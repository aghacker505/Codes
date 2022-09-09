from this import d


def num(a,b):
    '''here we will return multiple values'''
    c = a+b
    d = a-b
    return c, d

x, y = num(10, 20)
print("additon is: ", x)
print("substraction is: ",y)