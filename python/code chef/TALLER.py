# cook your dish here
#number of test cases
n = int(input())

while n>0:
    x = list(map(int , input().split()))
    if(x[0]>x[1]):
        print('a')
    else:
        print('b')
    n = n-1