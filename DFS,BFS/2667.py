# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def DFS(x,y):
    global k
    if x < 0 or x >= n or y < 0 or y >= n : 
        return False
    if graph[x][y] == 1:
        k += 1
        graph[x][y] = 0
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True
    return False

result = 0
num=[]
for i in range(n):
    for j in range(n):
        k = 0
        if DFS(i,j):
            num.append(k)
            result += 1
print(result)
num.sort()
print(*num,sep="\n")