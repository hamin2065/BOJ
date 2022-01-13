# https://www.acmicpc.net/problem/10867
# 중복 빼고 정렬하기
import sys
n = int(input())

s = set(map(int, sys.stdin.readline().strip().split()))
s = list(s)
s.sort()
print(*s)