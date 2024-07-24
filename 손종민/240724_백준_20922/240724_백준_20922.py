import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split(' '))
ls = list(map(int, input().split(' ')))
tmp = []
result = 0

for num in ls:
    if tmp.count(num) < K:
        tmp.append(num)
    else:
        if result < len(tmp):
            result = len(tmp)
        tmp = []

print(result)