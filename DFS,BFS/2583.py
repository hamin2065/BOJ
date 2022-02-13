# https://www.acmicpc.net/problem/2583
# 영역 구하기
import sys
sys.setrecursionlimit(100000) 
# m -> y좌표, n -> x 좌표
m, n, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

def paint(l_x,l_y,r_x,r_y) : 
    x = r_x - l_x
    y = r_y - l_y
    for i in range(x) : 
        for j in range(y) : 
            graph[l_x+i][l_y+j] = 1

for _ in range(k) : 
    l_x,l_y,r_x,r_y = map(int, input().split())
    paint(l_x,l_y,r_x,r_y)
arr = []    
def dfs(x,y) : 
    global num
    if x < 0 or x >= n or y < 0 or y >= m : return
    if graph[x][y] == 0 : 
        num += 1
        graph[x][y] = 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result = 0
for i in range(n) : 
    for j in range(m) : 
        num = 0
        if dfs(i,j) : 
            arr.append(num)
            result += 1
            
print(result)
arr.sort()
print(*arr)