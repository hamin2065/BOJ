n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

result = 0
for i in range(n) : 
    b = max(B)
    result += A[i]*b
    B.pop(B.index(b))
print(result)