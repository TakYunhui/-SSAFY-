# 20310 타노스

import sys

sys.stdin = open('input.txt')

# input 받아와서
# 0과 1을 분리해서 저장한 뒤
# 절반 개수의 0을 출력하고, 그 뒤 절반 개수의 1 출력

N = input()
zeros = []
ones = []

for number in N:
    if number == '0':
        zeros.append(number)
    elif number == '1':
        ones.append(number)

print(zeros)
print(ones)