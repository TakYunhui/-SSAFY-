import sys

sys.stdin = open('input.txt')

N = int(input())
li = []

for _ in range(N):
    li += list(map(int, input().split(' ')))

li.sort(reverse=True)
print(li[N-1])