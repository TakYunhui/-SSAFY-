import sys

sys.stdin = open('input.txt')

N = int(input())

days = []
for _ in range(N):
    day = list(map(int, input().split(' ')))
    days.append(day)

results = []
# 모든 경우를 보기 위한 For문
for i in range(N):
    today = days[i][0]
    result = days[i][1]
    while today < N:
        for j in range(today, N):
            if today + days[j][0] <= N:
                today += days[j][0]
                result += days[j][1]
    results.append(result)

print(results)    