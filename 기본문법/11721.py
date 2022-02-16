# https://www.acmicpc.net/problem/11721
# 열 개씩 끊어 출력하기

str = input()
for i in range(len(str)//10+1):
    print(str[i*10:(i+1)*10])