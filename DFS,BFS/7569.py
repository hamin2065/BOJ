# https://www.acmicpc.net/problem/7569
# 토마토

from collections import deque

m, n, h = map(int, input().split())

tomato = []

for _ in range(h) :
    arr = []
    for _ in range(n) : 
        arr.append(list(map(int, input().split())))
    tomato.append(arr)


# [i][j][k] -> i는 z축, j는 y축, k는 x축

ripen = deque([])

for i in range(h) : 
    for j in range(n) : 
        for k in range(m) : 
            if tomato[i][j][k] == 1 : 
                ripen.append((k,j,i))
                
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
count = 0

while ripen : 
    for _ in range(len(ripen)) : 
        x,y,z = ripen.popleft()
        for i in range(6) : 
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h : 
                continue
            if tomato[nz][ny][nx] == -1 : # 벽인 경우
                continue
            if tomato[nz][ny][nx] == 0 : 
                tomato[nz][ny][nx] = 1
                ripen.append((nx, ny, nz))
    count += 1
            
print(-1 if '0' in str(tomato) else count-1)