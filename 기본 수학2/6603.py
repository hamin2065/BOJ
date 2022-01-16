# https://www.acmicpc.net/problem/6603
# 로또
import sys
from itertools import combinations

def lotto():
    while True:
        lot= list(map(int, sys.stdin.readline().strip().split()))
        if lot[0] == 0:
            return
        else:
            a = list(combinations(lot[1:],6))
            for i in a:
                print(*i)
            print()
lotto()