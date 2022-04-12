# https://www.acmicpc.net/problem/1002
# 터렛

import math

def sol(x1, y1, r1, x2, y2, r2) : 
    # (x1, y1)이 중심, r1이 반지름. (x2, y2)이 중심, r2가 반지름인 원의 교점 개수
    if x1 == x2 and y1  == y2 :
        if r1 == r2: return -1
        else : return 0
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dis == r1 + r2 : return 1
    elif dis > r1 + r2 : return 0
    elif dis == abs(r1-r2) : return 1
    elif dis < abs(r1-r2) : return 0
    else : return 2

test = int(input())

for _ in range(test) : 
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(sol(x1, y1, r1, x2, y2, r2))