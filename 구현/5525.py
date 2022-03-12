''' 50점 코드
def check(c,s) : 
    for i in range(len(c)) : 
        if c[i] != s[i] : 
            return False
    return True
n = int(input())
m = int(input())
s = list(input())
c = "IO"*n+"I"
result = 0
for i in range(m-(2*n+1)) : 
    if s[i] == "I" : 
        if check(c,s[i:i+2*n+1]) : 
            result += 1
print(result)
'''

n = int(input())
m = int(input())
s = input()

idx = 1;check = 0;answer=0
while idx < m-1 : 
    if s[idx:idx+3] == "IOI" : 
        check += 1
        idx += 2
        if check == n : 
            check -= 1
            answer += 1
    else : 
        check = 0
        idx += 1
print(answer)