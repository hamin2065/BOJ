# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    l = len(citations)
    citations.sort()
    for idx, citation in enumerate(citations) : 
        if citation >= l-idx : 
            return l-idx
    return 0