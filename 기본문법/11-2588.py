# 곱셈
# https://www.acmicpc.net/problem/2588

a = int(input())
b = input()
list=[]
c = 0
for i in range(len(b)-1,-1,-1):
    list.append(a*int(b[i]))
    print(list[-1])
    c += list[-1]*(10**(2-i))
print(c)