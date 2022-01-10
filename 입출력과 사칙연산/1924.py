# https://www.acmicpc.net/problem/1924
# 2007년

x,y = map(int, input().split())
day_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
days = y
for i in range(1,x):
    if i == 2:days += 28
    elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:days += 31
    else:days+= 30
print(day_list[(days-1)%7])