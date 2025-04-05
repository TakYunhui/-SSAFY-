# 실버 3. 게으른 백곰
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
buckets = list()

for _ in range(n):
    g, x = map(int, input().split())
    buckets.append((x, g)) # 좌표, 양
buckets.sort() # 좌표 순 정렬

# 자리로부터 -k ~ +k만큼 양동이 사용 가능
l, r, tmp = 0, 0, 0
answer = 0
while l <= r and r < n:
    # 현재 끝 인덱스의 양동이와 현재 시작 인덱스의 양동이의 차가 2 * k 이하라면
    # 끝 인덱스 양동이 값을 임시 합에 추가, 끝 인덱스 옮기기
    if buckets[r][0] - buckets[l][0] <= 2 * k:
        tmp += buckets[r][1]
        answer = max(answer, tmp)
        r += 1
    # 2 * k보다 크면 조건에 안 맞으니 양동이 하나 뺀다, 시작 인덱스 바꿈
    else:
        tmp -= buckets[l][1]
        l += 1
print(answer)