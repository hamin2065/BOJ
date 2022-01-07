# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

strs = input().split('-')

a=[]
for str in strs:
    if str.isdigit():
        str = int(str)
    else:
        result=0
        temp_arr = str.split('+')
        for i in range(len(temp_arr)):
            result+=int(temp_arr[i])
        str = result
    a.append(str)

num = a[0]
for i in range(1,len(a)):
    num -= a[i]
print(num)