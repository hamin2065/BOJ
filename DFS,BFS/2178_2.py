from collections import deque

n,m = map(int, input().split())

maze = []
for i in range(n) : 
    maze.append(list(map(int, input())))
visited = [[False for _ in range(m)]for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
    
def solve() : 
    que = deque([(0,0)])
    visited[0][0] = True
    while que : 
        for _ in range(len(que)) : 
            nx,ny = que.popleft()
            for i in range(4) : 
                x = nx+dx[i]
                y = ny+dy[i]
                if 0<=x<m and 0<=y<n and visited[y][x] == False: 
                    if maze[y][x] != 0 :
                        maze[y][x] = maze[ny][nx]+1
                        visited[y][x] = True
                        que.append((x,y))
    return maze[n-1][m-1]
print(solve())