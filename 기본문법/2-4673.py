# 셀프 넘버
# https://www.acmicpc.net/problem/4673

# 하나의 수가 주어졌을 때 그 수로 만들 수 있는 모든 수
def self_number(n):
    while n <= 10000:
        self_n = sum(map(int, str(n))) + n
        if self_n <= 10000 and x[self_n] == 0:
            x[self_n] = 1
        else:pass
        n = self_n
    return

# 0은 셀프 넘버 아니라는 뜻
x = [0 for _ in range(10001)]
x[0] = 1

for i in range(1,10001):
    self_number(i)

for i,j in enumerate(x):
    if j == 0:print(i)
    