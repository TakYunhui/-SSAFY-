import sys

sys.stdin = open('input.txt')

N = int(input())

stair = [int(input()) for _ in range(N)]

result = 0
index = 0

# 역순으로
for i in range(0, N, -1):
    print(stair[i])