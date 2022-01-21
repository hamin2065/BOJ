# https://www.acmicpc.net/problem/2512
# 예산

n = int(input())
money = list(map(int, input().split()))
amount = int(input())

start = 0
end = max(money)
cnt = 0
while start <= end : 
    total = 0
    mid = (start+end)//2
    for i in money:
        if mid < i:
            total += mid
        else : 
            total += i
    # total = amount일때 상한값이 더 커도 성립할 가능성 o 
    if total <= amount : 
        start = mid + 1
    else : 
        end = mid - 1
print(end)