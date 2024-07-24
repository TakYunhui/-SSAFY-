import sys

sys.stdin = open('input.txt')

N = int(input())

ls = []
max_high = 0
last_column = 0
for _ in range(N):
    L, H = map(int, input().split(' '))
    ls.append((L, H))
    if H > max_high:
        max_high = H
    if L > last_column:
        last_column = L = L


ls.sort()

result = 0
current_height = 0
checker = 0
for i in range(last_column):
    # 하나씩 체크하면서 위치에 따라 갱신해주기
    if i < ls[checker][0]:
        result += current_height
    else:        
        result += current_height
        checker += 1
        if current_height < ls[checker][1]:
            current_height = ls[checker][1]

print(result)