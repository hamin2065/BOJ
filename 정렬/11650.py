# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기
import sys
n = int(input())
coor = []
for i in range(n):
    x,y = map(int, sys.stdin.readline().strip().split())
    coor.append((x,y))
coor.sort(key = lambda x : (x[0],x[1]))

for i in range(n):print(str(coor[i][0])+" "+str(coor[i][1]))

