# 실버 3. 게임
# 게임을 몇 번 더 이기면 승률이 변하는지 확인
x, y = map(int, input().split())
# z = int((y / x) * 100) 정수형 변환으로 부동 소수점 연산에 오차가 생김
z = (y * 100) // x
# x번만큼 게임을 더하면 승률이 99로 변하기에 최대 x번까지 반복
left = 0
right = x
result = z # 승률 변하는 것 기록용

# 승률이 99 이상으로 커질 수 없음 - 변할 수 없음
if z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        # mid번 더 게임 진행 한 뒤 승률이 오른다면
        if ((y + mid) * 100) // (x + mid) > z:
            result = mid # 승률 갱신
            right = mid - 1
        else:
            left = mid + 1
    print(result)


