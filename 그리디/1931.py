# https://www.acmicpc.net/problem/1931
# 회의실 배정
n = int(input())
rooms = []
for i in range(n):
    a,b = map(int, input().split())
    rooms.append((a,b))
rooms.sort(key = lambda x : (x[1],x[0]))

finish = rooms[0][1]
count =1
   
for i in range(1,n):
    if finish <= rooms[i][0]:
        count += 1
        finish = rooms[i][1]
print(count)