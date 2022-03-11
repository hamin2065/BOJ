n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

d = dict()

for i in A :
    if i in d : 
        d[i] += 1
    else : 
        d[i] = 1
        
for i in B : 
    if i in d : 
        print(d[i], end = ' ')
    else :
        print(0, end=' ')