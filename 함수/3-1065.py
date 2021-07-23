# 한수
# https://www.acmicpc.net/problem/1065

def check(n):
    list_1 = list(map(int, str(n)))
    if len(list_1) <= 2:return True
    x = list_1[1] - list_1[0]
    for i in range(1,len(list_1)-1):
        if list_1[i+1] - list_1[i] != x:
            return False
    return True

n = int(input())
a = 0
for i in range(1,n+1):
    if check(i) == True:a += 1
print(a)