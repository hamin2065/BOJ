# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations
import math
def solution(numbers):
    arr = []
    for i in range(1,len(numbers)+1) : 
        for j in permutations(list(numbers),i) :
            s = ""
            for k in j : 
                s += k
            if sol(int(s)) == True : # 소수인 경우
                arr.append(int(s))
    answer = 0
    return len(set(arr))

def sol(num) : 
    if num <= 1 : return False
    for i in range(2, int(math.sqrt(num)) + 1) : 
        if num % i == 0 :
            return False
    return True