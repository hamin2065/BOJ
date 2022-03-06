# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

n = int(input())
result = 1
for i in range(n,0,-1) : 
    result *= i
count = 0
result = str(result)

for i in range(len(result)-1,-1,-1) : 
    if result[i] == '0' : 
        count += 1
    else : break
    
print(count)