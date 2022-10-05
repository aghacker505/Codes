# There is a cricket match going on between two teams AA and BB.
# Team BB is batting second and got a target of XX runs. Currently, team BB has scored YY runs. Determine how many more runs Team BB should score to win the match.
# Note: The target score in cricket matches is one more than the number of runs scored by the team that batted first.

#nuber of input cases
n = int(input())

while n > 0:
    x = list(map(int, input().split()))
    print(x[0] - x[1])
    n = n - 1