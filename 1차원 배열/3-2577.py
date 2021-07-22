# 숫자의 개수
# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

n = A*B*C
n = str(n)
num_list = [0 for _ in range(10)]
for i in n:
    num_list[int(i)] += 1

for i in range(len(num_list)):
    print(num_list[i])