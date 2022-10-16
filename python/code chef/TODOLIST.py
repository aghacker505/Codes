# cook your dish her
#number of test cases
T = int(input())
while T>0:
    #total number of problems added in the To-DO list
    N = int(input())
    lst = list(map(int , input().split()))
    rem = 0
    for i in lst:
        if i>=1000:
            rem = rem+1
    print(rem)
    T = T-1
            