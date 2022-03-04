# https://www.acmicpc.net/problem/1780
# 종이의 개수

from sys import stdin

n = int(input())
arr = [list(map(int, stdin.readline().strip().split())) for _ in range(n)]
minus = zero = plus = 0
def solve(x,y,n) : 
    global minus,zero,plus
    curr = arr[x][y]
    for i in range(x,x+n) : 
        for j in range(y,y+n) : 
            if curr != arr[i][j] :
                for k in range(3) : 
                    for l in range(3) :
                        solve(x+k*n//3,y+l*n//3,n//3)
                return
            
    if curr == -1 : 
        minus += 1
    elif curr == 0:
        zero += 1
    else : 
        plus += 1
solve(0,0,n)      
print(minus,zero,plus,sep="\n")