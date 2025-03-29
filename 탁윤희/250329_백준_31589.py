# 실버 3. 포도주 시음
n, k = map(int, input().split())
wines = sorted(list(map(int, input().split())))
# 포도주 2종류 차이만큼 맛을 느낌 + 제일 처음 마시는 포도주는 본연의 맛
# 제일 맛 좋은 걸 하나 먼저 마신다, 그 다음 두 포인터로 차가 최대로 나는 종류 선택
# 즉 최고(1순위) - 최저(1순위) - 최고(2순위) - 최저(2순위) 이런 느낌으로 차이 주며 마신다
answer = wines[-1] # wine 맛의 합 누적
l, r = 0, n-1 # 와인 고르는 순위 인덱스
cnt = 1 # wine 종류 갯수 누적

while cnt < k:
    if cnt == 1:
        r -= 1 # 다음 최고 2순위 고름
        cnt += 1
    else:
        # cnt 홀수일 때, 최저 순위 고른다
        if cnt % 2:
            r -= 1
            cnt += 1
        else:
            answer += wines[r] - wines[l]
            cnt += 1
            l += 1

print(answer)