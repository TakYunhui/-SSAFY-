# 19637 IF문 좀 대신 써줘
import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split(' '))
titles = []
for _ in range(N):
    title = list(map(str, input().split(' ')))
    titles.append(title)

for _ in range(M):
    power = int(input())
    for title in titles:
        if power <= int(title[1]):
            print(title[0])
            break