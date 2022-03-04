n = int(input())
rope = [int(input()) for _ in range(n)]

rope.sort()
current = 0

for i in range(n) : 
    if current <= rope[i]*(n-i) : 
        current = rope[i] *(n-i)
print(current)