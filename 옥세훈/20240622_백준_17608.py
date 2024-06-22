# 막대기
# 브2
import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    num = int(input())
    ls.append(num)


last_num = ls.pop()
result = 1

for i in range(n-1):
    check_num = ls.pop()
    if check_num > last_num:
        last_num = check_num
        result += 1

print(result)
