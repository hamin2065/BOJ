# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    brown = (brown-4)//2
    r=0
    for i in range(1, brown+1) : 
        if i*(brown-i) == yellow : 
            r = i
            break
    answer = [max(r+2, brown-r+2),min(r+2, brown-r+2)]
    return answer