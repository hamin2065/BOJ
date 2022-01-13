# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2
import sys
n = int(input())
coor = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().strip().split())
    coor.append((x,y))
coor.sort(key = lambda x : (x[1],x[0]))

for i in range(n):print(str(coor[i][0])+" "+str(coor[i][1]))

