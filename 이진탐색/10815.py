# https://www.acmicpc.net/problem/10815
# 숫자 카드

import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for index, value in enumerate(check):
    check[index] = (index, value)

cards.sort()
check.sort(key = lambda x:x[1])
i=j=0
result = [0]*len(check)
while i< len(cards) and j < len(check):
    if cards[i] == check[j][1]:
        result[check[j][0]] = 1
        i += 1
    elif cards[i] < check[j][1]:
        i += 1
    else:j += 1

print(*result)