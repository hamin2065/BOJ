# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

s = input()

list = ['c=','c-','d-','lj','nj','s=','z=']
i = 0
sum = 0
while i < len(s):
    if i+2 <= len(s)-1:
        if s[i:i+3] == 'dz=':
            sum += 1
            i += 3
        elif s[i:i+2] in list:
            sum += 1
            i += 2
        else:
            sum += 1
            i += 1
    elif i+1 <= len(s)-1:
        if s[i:i+2] in list:
            sum += 1
            i += 2
        else:
            sum += 1
            i += 1
    else:
        sum += 1
        i += 1

print(sum)
        
# count method..