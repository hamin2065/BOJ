# https://www.acmicpc.net/problem/1181
# 단어 정렬
'''
import sys
n = int(input())
words=[]

for i in range(n):
    word = sys.stdin.readline().strip()
    words.append((len(word),word))
words.sort(key = lambda x:(x[0],x[1]))

print(words[0][1])
for i in range(1,n):
    if words[i][1] == words[i-1][1]:continue
    print(words[i][1])
'''
'''
import sys
n = int(input())
words = set()
for i in range(n): 
    words.add(sys.stdin.readline().strip())
words = list(words)

words.sort()
words.sort(key = lambda x : len(x))
print("\n".join(words))'''
