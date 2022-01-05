# 이것이 취업을 위한 코딩 테스트다 p.115
# 왕실의 나이트

str = input()
char = ord(str[0])-ord('a')+1
num = int(str[1])
result = 0

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

for step in steps:
    if char+step[0]>=1 and char+step[0]<=8 and num+step[1] >= 1 and num+step[1]<= 8:result += 1
print(result)