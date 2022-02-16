# https://www.acmicpc.net/problem/14889
# 스타트와 링크

from itertools import combinations

n = int(input())

teams = [i for i in range(n)]

powers = []

for i in range(n) : powers.append(list(map(int, input().split())))

# 팀나누기.
divide_team = list(combinations(teams, n//2))

l = len(divide_team)
arr = []

for t in range(len(divide_team)//2) : 
    start = 0
    link = 0
    for i in divide_team[t] : 
        for j in divide_team[t] : 
            start += powers[i][j]
    for i in divide_team[l-1-t] : 
        for j in divide_team[l-1-t] : 
            link += powers[i][j]
    arr.append(abs(start-link))
   
print(min(arr))