# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

def group_word(s):
    word_list = []
    for i,j in enumerate(s):
        word_list.append((j,i))
    word_list.sort()
    for i in range(len(word_list)-1):
        if word_list[i][0] == word_list[i+1][0]:
            if word_list[i][1] - word_list[i+1][1] != -1:
                return False
    return True

n = int(input())
sum = 0
for _ in range(n):
    if group_word(input()) == True: sum += 1
print(sum)
