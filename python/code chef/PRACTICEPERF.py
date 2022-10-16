ans = 0

list = list(map(int, input().split()))

for i in range(0, 4):
    if list[i] >= 10:
        ans +=1

print(ans)
