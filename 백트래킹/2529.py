# https://www.acmicpc.net/problem/2529
# 부등호

n = int(input())
arr = input().split()

visited = [False] * 10
min_value, max_value = "",""
def check(i,j,k) : 
    if k == ">" : 
        return i > j
    else : 
        return i < j
    
def solve(idx, result) : 
    global min_value,max_value
    if idx == n + 1 : 
        if len(min_value) == 0 : 
            min_value = result
        else : 
            max_value = result
        return
    for i in range(10) : 
        if visited[i] == False : 
            if idx == 0 or check(result[-1],str(i),arr[idx-1]) : 
                visited[i] = True
                solve(idx+1, result + str(i))
                visited[i] = False
solve(0,"")                
print(max_value)
print(min_value)