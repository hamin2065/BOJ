# https://www.acmicpc.net/problem/2480
# 주사위 세개

a, b, c = map(int, input().split())

if a == b and a == c and b == c : # 1번 경우
    print(10000+a*1000)
elif a != b and a != c and b != c : #3번 경우
    print(max(a, b, c)*100)
else : 
    if a == b : print(a*100 + 1000)
    elif a == c : print(a*100 + 1000)
    else : print(b*100 + 1000)