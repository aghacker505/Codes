def fac(n):
    prod = 1
    while n>=1:
        prod = prod*n
        n-=1

    return prod

#display factorial of first 10 numbers
# calling fac() funnction and passing value from 1 to 11
end = int(input('Enter the number of factorial value: '))
for i in range(1,end):
    print('Factorial of {} is {}'.format(i, fac(i)))