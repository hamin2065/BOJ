# 나머지
# https://www.acmicpc.net/problem/3052

mod_list = [0 for _ in range(42)]

for _ in range(10):
    n = int(input())
    mod_list[n%42] += 1

print(42 - mod_list.count(0))