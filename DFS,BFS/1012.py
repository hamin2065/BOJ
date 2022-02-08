# https://www.acmicpc.net/problem/1012
# 유기농 배추

import sys
sys.setrecursionlimit(10**6)
def solve(a,b,n,m,arr):
    if a <= -1 or a >= m or b <= -1 or b >= n:
        return False
    if arr[a][b] == 1 : 
        arr[a][b] = 0
        solve(a-1,b,n,m,arr)
        solve(a+1,b,n,m,arr)
        solve(a,b-1,n,m,arr)
        solve(a,b+1,n,m,arr)
        return True
    return False
num = int(input())

for _ in range(num) : 
    m,n,k = map(int, sys.stdin.readline().strip().split())
    arr = [[0 for _ in range(m)]for _ in range(n)]
    for _ in range(k) : 
        x,y = map(int, sys.stdin.readline().strip().split())
        arr[y][x] = 1
    result = 0
    for i in range(n) : 
        for j in range(m) : 
            if solve(i,j,m,n,arr) == True : 
                result += 1
    print(result)