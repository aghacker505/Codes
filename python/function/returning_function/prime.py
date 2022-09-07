def prime(n):
    ''' to check if n is prime or not'''
    x = 1 #this will be 0 if not prime 
    for i in range (2,n):
        if n%i == 0:
            x = 0
            break
        else:
            x = 1
    return x

num = int(input('Enter any number: '))

result = prime(num)
if result == 1:
    print(num, 'is prime')

else:
    print(num, 'is not prime')