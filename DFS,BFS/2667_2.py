n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

def DFS(a,b) : 
    global result
    if a<0 or a>= n or b<0 or b>= n : return False
    if graph[a][b] == 1 : 
        result += 1
        graph[a][b] = 0
        DFS(a+1,b)
        DFS(a-1,b)
        DFS(a,b+1)
        DFS(a,b-1)
        return True
    return False

arr =[]

for i in range(n):
    for j in range(n) : 
        result = 0
        if DFS(i,j) == True : 
            arr.append(result)
print(len(arr))
arr.sort()
print(*arr,sep="\n")
            
