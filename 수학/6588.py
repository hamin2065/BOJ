# https://www.acmicpc.net/problem/6588
# 골드바흐의 추측

n=1000000

check = [True for _ in range(n)]

for i in range(2,int(n**0.6)):
    if check[i]==True:
        for j in range(i*2, n, i) : 
            if check[j] == True :
                check[j] = False 

def Gold(num) : 
    for i in range(3, num) : 
        if check[i] and check[num-i] : 
            return i, num-i        

while True : 
    num = int(input())
    if num == 0 : break
    left, right = Gold(num)
    print(left+right,"=",left,"+",right)
    
        
        
        