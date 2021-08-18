# 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775

def count_people(a,b):
    for i in range(a):
        x = 0
        for j in range(b):
            x += list[i][j]
            list[i+1].append(x)
    return list

n = int(input()) # TC 개수

for i in range(n):
    list = [[]*i for i in range(15)]
    list[0] = [i+1 for i in range(15)]
    a = int(input()) #층
    b = int(input()) #호
    lis = count_people(a,b)
    print(list[a][b-1])