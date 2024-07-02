# 20310 타노스

import sys

sys.stdin = open('input.txt')

# input 받아와서
# 0과 1을 분리해서 저장한 뒤
# 절반 개수의 0을 출력하고, 그 뒤 절반 개수의 1 출력

# 반례 : 0이 나왔다 1이 나왔다 다시 0이 나오는 경우


N = input()
zeros = []
ones = []


for number in N:
    if number == '0':
        zeros.append(number)
    elif number == '1':
        ones.append(number)

result = ""
for i in range(len(zeros) // 2):
    result += zeros[i]

for i in range(len(ones) // 2):
    result += ones[i]

print(result)