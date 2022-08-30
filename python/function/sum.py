# def sum():
#     a = int(input('Enter the number: '))
#     b = int(input('Enter the number: '))
#     c = a + b
#     print('Sum is: ', c)

# sum()
'''
-------------------ABOVE CODE CAN ALSO WRITTEN AS---------------------------'''

def sum(a, b):
    c = a + b
    return c

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

print('Sum is: ', sum(x, y))