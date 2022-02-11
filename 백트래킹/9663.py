# https://www.acmicpc.net/problem/9663
# N-Queen

def check(k) : 
    for i in range(k) : # i행, arr[i]열
        if arr[k] == arr[i] : return False
        if abs(arr[k]-arr[i]) == k-i : return False
    return True

# idx는 행        
def solve(idx) : 
    global result
    if idx == n : 
        result += 1
        return
    for i in range(n) : 
        arr[idx] = i
        if check(idx) : 
            solve(idx+1)    
            
n = int(input())

# i번째 행 arr[i]열
arr = [0 for _ in range(n)]
result = 0
solve(0)           
print(result)