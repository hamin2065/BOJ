# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

s = input()
result = [-1 for _ in range(26)]

for i in range(len(s)):
    if result[ord(s[i])-97] != -1 : pass
    else : result[ord(s[i])-97] = i

for i in range(26):
    print(result[i], end= ' ')