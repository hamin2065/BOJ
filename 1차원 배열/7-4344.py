# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

def average(x):
    a = x[0]
    people = 0
    avg = (sum(x)-x[0])/x[0]
    for i in range(1,a+1):
        if x[i] > avg: people += 1
    return people

n = int(input())
for i in range(n):
    x = list(map(int, input().split()))
    result = average(x)/x[0]*100
    print(format(result, ".3f"),end='')
    print("%")