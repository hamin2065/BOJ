# https://www.acmicpc.net/problem/2110
# 공유기 설치

from sys import stdin

n, c = map(int, stdin.readline().strip().split())
home = [int(stdin.readline().strip()) for _ in range(n)]

home.sort()

# start = 최소거리;end = 최대거리
start = 1;end=home[-1]-home[0]
while start <= end : 
    mid = (start + end) // 2 # 간격
    current = home[0] # 현재 집 위치
    count = 1
    for i in range(n):
        if home[i] >= current + mid : 
            count += 1
            current = home[i]
    if count >= c : 
        start = mid + 1
        answer = mid
    else : 
        end = mid - 1
print(answer)