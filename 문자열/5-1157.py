# 단어 공부
# https://www.acmicpc.net/problem/1157
s = list(input().upper())
result = [0 for _ in range(26)]

for i in s:
    result[ord(i)-65] += 1

max = max(result)
max_index = result.index(max)
result[max_index] = 0
if max in result:print("?")
else:print(chr(max_index+65))