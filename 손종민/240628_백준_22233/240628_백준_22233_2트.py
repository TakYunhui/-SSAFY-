# 22233 가희의 메모장
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split(" "))

memo = []
for _ in range(N):
    memo.append(input())

keyword = []
result = len(memo)
words = set()
for _ in range(M):
    words.add(map(str, input().split(",")))

print(words)


