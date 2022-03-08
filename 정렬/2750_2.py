import sys

n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))
_B = []
for i in range(m) : 
    _B.append([B[i],i,0])

A.sort()
_B.sort()
j = 0;i = 0
while True :
    if j == n or i==m : break
    if A[j] == _B[i][0] : 
        _B[i][2] = 1
        i += 1;j+=1
    elif A[j] < _B[i][0] : 
        j += 1
    else :
        i += 1
        
_B.sort(key = lambda x : x[1])

for i in range(m) : 
    print(_B[i][2],end = ' ')