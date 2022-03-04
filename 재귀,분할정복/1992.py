# https://www.acmicpc.net/problem/1992
# 쿼드트리

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
result = []

def solve(x,y,n) : 
    curr = arr[x][y]
    for i in range(x,x+n) : 
        for j in range(y,y+n) : 
            if curr != arr[i][j] : 
                curr = -1
                break

    if curr == -1 : 
        n=n//2
        print("(",end='')
        solve(x,y,n)
        solve(x,y+n,n)
        solve(x+n,y,n)
        solve(x+n,y+n,n)
        print(")",end='')
    else : 
        print(curr,end='')
solve(0,0,n)
