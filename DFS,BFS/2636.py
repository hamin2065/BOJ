# https://www.acmicpc.net/problem/2636
# 치즈

from collections import deque

n, m = map(int, input().split()) # 세로, 가로

cheese = []

for _ in range(n) :
    cheese.append(list(map(int, input().split())))
# [i][j] # 세로, 가로


ans = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS() : 
    Q = deque([])
    Q.append([0,0])
    visited[0][0] = 1
    count = 0
    while Q : 
        y,x = Q.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[ny][nx] == 1: 
                continue
            if cheese[ny][nx] == 0 : 
                visited[ny][nx] = 1
                Q.append([ny, nx])
            elif cheese[ny][nx] == 1 : 
                cheese[ny][nx] = 0
                visited[ny][nx] = 1
                count += 1
    ans.append(count)
    return count
time = 0
while True : 
    time += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = BFS()
    if count == 0 : 
        break
print(time-1)
print(ans[-2])
