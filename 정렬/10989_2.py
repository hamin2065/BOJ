import sys


n = int(input())

A = [0 for _ in range(10001)]

for i in range(n) : 
    num = int(sys.stdin.readline().strip())
    A[num] += 1


for i in range(10001) : 
    if A[i] != 0 : 
        for j in range(A[i]) : 
            print(i)
            