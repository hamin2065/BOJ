# https://www.acmicpc.net/problem/15686
# 치킨 배달

from itertools import combinations

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

# 0 -> 빈 칸, 1 -> 집, 2 -> 치킨집

chicken = []
house = []

for i in range(n) : 
    for j in range(n) : 
        if city[i][j] == 2 : 
            chicken.append((i,j))
        elif city[i][j] == 1 : 
            house.append((i,j))

chicken_street = []

# 각각의 치킨집마다 치킨 거리 다 구함
for chi in combinations(chicken, m) :
    dis = [1e9 for _ in range(len(house))]
    for i in range(m) : 
        x, y = chi[i]
        for j in range(len(house)) : 
            d = abs(x-house[j][0]) + abs(y-house[j][1])
            if dis[j] > d : 
                dis[j] = d
    chicken_street.append(sum(dis))
print(min(chicken_street))
    