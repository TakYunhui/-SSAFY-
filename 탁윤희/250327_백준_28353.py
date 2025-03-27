# 실버 3. 고양이 카페
n, k = map(int, input().split())
cats = sorted(list(map(int, input().split())))
# 시작, 종료 인덱스
l, r = 0, n-1
answer = 0

while l < r:
    tmp = cats[l] + cats[r]
    # 2마리 무게 합이 k 이하라면 조건에 맞으니 행복해지는 사람 수 추가
    # 조건에 맞는 2마리 썼으니까 왼쪽 인덱스 늘리고, 오른쪽 인덱스 줄여서 다음 2마리 확인
    if tmp <= k:
        answer += 1
        l += 1
        r -= 1
    # 합이 k 초과하면 작은 수는 그대로 두고 큰 수 쪽을 줄여서 확인
    else:
        r -= 1

print(answer)
