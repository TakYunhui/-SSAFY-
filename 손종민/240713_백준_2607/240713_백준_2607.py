# 2607 비슷한 단어

import sys

sys.stdin = open('input.txt')

N = int(input())
firstWord = [spell for spell in input()]

result = 0
for _ in range(N - 1):
    word = [spell for spell in input()]
    tmp = 0
    # 첫번째, 길이 차이가 많이 날 때
    
    for i in range(len(firstWord)):
        tmp = word.count(firstWord[i])
        if tmp == 0:
            break
    if tmp != 0:
        result += 1

print(result)