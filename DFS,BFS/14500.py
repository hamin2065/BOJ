# https://www.acmicpc.net/problem/14500
# 테트로미노

def solve(idx,x,y,sub_sum) : 
    global result
    if result >= sub_sum + max_value*(3-idx) : return
    if idx == 3 : 
        result = max(result, sub_sum)
        return
    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m  and visited[nx][ny] == 0 : 
            if idx == 1 : 
                visited[nx][ny] = 1
                solve(idx+1, x, y, sub_sum + arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            solve(idx+1, nx, ny, sub_sum+arr[nx][ny])
            visited[nx][ny] = 0
    
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result=0
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
max_value = max(map(max, arr)) # 전체 배열에서 가장 큰 값

for i in range(n) : 
    for j in range(m) : 
        visited[i][j] = 1
        solve(0,i,j,arr[i][j])
        visited[i][j] = 0
print(result)