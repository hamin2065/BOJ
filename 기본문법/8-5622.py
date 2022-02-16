# 다이얼
# https://www.acmicpc.net/problem/5622

s = input()

list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result = 0
for i in s:
    if i in list[0]:result += 3
    elif i in list[1]:result += 4
    elif i in list[2]:result += 5
    elif i in list[3]:result += 6
    elif i in list[4]:result += 7
    elif i in list[5]:result += 8
    elif i in list[6]:result += 9
    elif i in list[7]:result += 10
print(result)
