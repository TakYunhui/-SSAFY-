# 1138 줄 세우기
# 인덱스로 접근하면 될 것 같은데...
# 정렬을 작은 순서부터? 큰 순서부터?
import sys

sys.stdin = open('input.txt')


N = int(input())

onleft = list(map(int, input().split(' ')))
result = [0 for _ in range(N)]

# 키 작은 순부터 살펴보기
for i in range(N):
    # onleft[i]와 비교하기 위한 count
    count = 0
    for j in range(N):
        if count == onleft[i] and result[j] == 0:
            # print('도착')
            result[j] = i + 1
            break
        elif result[j] == 0:
            count += 1

print(*result)