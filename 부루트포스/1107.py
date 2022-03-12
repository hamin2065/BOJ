# https://www.acmicpc.net/problem/1107
# 리모컨

from sys import stdin

n = int(input())
ans = abs(100-n)
m = int(input())
if m != 0 : 
    buttons = list(map(int,stdin.readline().strip().split()))
else : 
    buttons = []
    
for num in range(1000001) : 
    num = str(num)
    for i in range(len(num)) : 
        if int(num[i]) in buttons : 
            break
        elif i == len(num)-1 : 
            # 기존닶, 번호 누른 횟수 + 해당번호로부터 n까지의 차이
            ans = min(ans, len(num)+abs(int(num)-n))
            
print(ans)