# https://www.acmicpc.net/problem/1026
# 보물

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
    
A.sort()
B.sort()

print(sum(A[i]*B[n-1-i] for i in range(n)))    
