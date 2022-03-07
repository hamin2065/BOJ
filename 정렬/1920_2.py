n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

_B = [(B[i],i)for i in range(m)]
check = [False]*m
A.sort()
_B.sort()
j = 0;i = 0
while True : 
    if i == m or j == n : break
    if _B[i][0] == A[j] : 
        check[_B[i][1]] = True
        i += 1
    elif _B[i][0] < A[j] : 
        i += 1
    else : 
        j += 1
        
for i in range(m) : print(1 if check[i] == True else 0)