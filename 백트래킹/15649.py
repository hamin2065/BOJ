# https://www.acmicpc.net/problem/15649
# N과 M (1)

n, m = map(int, input().split())

def solve(arr) : 
    if len(arr) == m : 
        print(*arr)
        return
    for i in range(1, n+1) : 
        if i in arr : continue
        solve(arr + [i])
arr = []
solve(arr)         