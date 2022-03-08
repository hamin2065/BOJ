import sys
n = int(input())
A = set()
for i in range(n) : 
    word = sys.stdin.readline().strip()
    A.add((word,len(word)))
A = list(A)
A.sort(key = lambda x : (x[1],x[0]))

for i in range(len(A)) : 
    print(A[i][0])