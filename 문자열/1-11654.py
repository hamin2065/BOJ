# 아스키 코드 
# https://www.acmicpc.net/problem/11654

a = input()

if type(a) == "<class 'int'>":
    print(chr(a))
else:
    print(ord(a))