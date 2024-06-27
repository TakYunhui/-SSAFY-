# 19941 햄버거 분배

import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split(' '))
table = []
for i in input():
    table.append(i)

count = 0

for i in range(N):
    # i번째가 사람이면
    if table[i] == 'P':
        if N >= K:
            if i - K < 0:
                for j in range(0, i + K + 1):
                    if table[j] == 'H':
                        count += 1
                        table[j] = 0
                        # print(j, '번째 햄버거')
                        # print(i, '번째 사람이 먹음')
                        break
            elif i + K + 1 > N:
                for j in range(i - K, N):
                    if table[j] == 'H':
                        count += 1
                        table[j] = 0
                        # print(j, '번째 햄버거')
                        # print(i, '번째 사람이 먹음')

                        break
            else:
                # print(i, '번째')
                # print(i-K, '부터', i+K, '탐색')
                for j in range(i - K, i + K + 1):
                    # print(j, '번째 항목')
                    if table[j] == 'H':
                        count += 1
                        table[j] = 0
                        # print(j, '번째 햄버거')
                        # print(i, '번째 사람이 먹음')
                        break
            # print(table)
        else:
            for j in range(N):
                if table[j] == 'H':
                    count += 1
                    table[j] = 0
                    break

print(count)