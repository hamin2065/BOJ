# 벌집
# https://www.acmicpc.net/problem/2292

# 1
# 2 - 7 (6)
# 8 - 19 (12)
# 20 - 37 (18)
# 38 - 61 (24)

n = int(input())
a = 2;b = 7;p = 6;i=1
while True:
    if n == 1:break
    if a <= n <= b:
        i += 1
        break
    else:
        a += p
        p += 6
        b += p
        i += 1
print(i)