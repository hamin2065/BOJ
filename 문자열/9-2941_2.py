# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

s = input()
print(len(s)-sum(map(s.count, ['c=','c-','dz=','d-','lj','nj','s=','z='])))