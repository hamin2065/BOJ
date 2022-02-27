# https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque
def solution(numbers, target):
    answer = 0
    Deq = deque()
    Deq.append((0,0))
    while Deq : 
        curr_sum, idx = Deq.popleft()
        if idx == len(numbers) : 
            if curr_sum == target : 
                answer += 1
        else : 
            Deq.append((curr_sum+numbers[idx],idx+1))
            Deq.append((curr_sum-numbers[idx], idx+1))
    return answer