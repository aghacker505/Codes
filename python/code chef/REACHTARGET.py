# cook your dish here
n = int(input())

while n > 0:
    x = list(map(int, input().split()))
    print(x[0] - x[1])
    n = n - 1