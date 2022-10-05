ans = 0

#creating a list with single line input()
lst = list(map(int, input().split()))

for i in range(0, 4):
    if lst[i] >= 10:
        ans +=1

print(ans)

# # cook your dish here
# P1 = int(input())
# P2 = int(input())
# P3 = int(input())
# P4 = int(input())
# ans = 0

# if P1 >= 10:
#     ans = ans+1
# if P2 >= 10:
#     ans=ans+1
# if P3 >= 10:
#     ans=ans+1
# if P4 >= 10:
#     ans= ans+1
    
# print(ans)