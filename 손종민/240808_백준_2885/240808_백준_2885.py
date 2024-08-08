import sys

sys.stdin = open('input.txt')

# N만큼 길이
# N은 2의 제곱
# N = 2**n
# 초콜렛을 쪼갠다...
# 재귀로?
K = int(input())

# [8]
# [4, 4]
# [2, 2, 4]
# [2, 2, 2, 2]
# [1, 1, 2, 2, 2, 2]
# [1, 1, 1, 1, 2, 2, 2]
# [1, 1, 1, 1, 1, 1, 2, 2]

n = 0
N = 2**n

chocos = list(N)
for choco in range(0, len(chocos), -1):
    if choco != 1:
        crush = chocos.pop(choco)
