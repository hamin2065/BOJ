# https://www.acmicpc.net/problem/1003
# 피보나치 함수

def fibo(x) : 
    DP[0] = [1,0]
    DP[1] = [0,1]
    for i in range(2,x+1) :
        DP[i][0] = DP[i-1][0] + DP[i-2][0]
        DP[i][1] = DP[i-1][1] + DP[i-2][1]
n = int(input())

for i in range(n):
    x = int(input())
    DP = [[0,0] for _ in range(41)]  
    fibo(x)
    print(DP[x][0],DP[x][1])