def color(l_x,l_y,r_x,r_y) : 
    for i in range(l_x,r_x) : 
        for j in range(l_y,r_y) : 
            graph[i][j] = 1

def DFS(x,y) : 
    global count
    if x<0 or x>= n or y<0 or y >= m : 
        return
    if graph[x][y] == 0 : 
        count += 1
        graph[x][y] = 1
        DFS(x+1,y)
        DFS(x-1,y)
        DFS(x,y+1)
        DFS(x,y-1)
        return True
    return False

m,n,k = map(int, input().split())

graph = [[0 for _ in range(m)]for _ in range(n)] #  [x][y]

for _ in range(k) : 
    l_x,l_y,r_x,r_y = map(int, input().split())
    color(l_x,l_y,r_x,r_y)
arr = []
result = 0
for i in range(n) : 
    for j in range(m) : 
        count = 0
        if DFS(i,j) == True : 
            arr.append(count)
            result += 1
            
print(result)
print(*sorted(arr))