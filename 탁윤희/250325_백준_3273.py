# 실버 3. 두 수의 합
# i + j 번째 수들의 합이 x를 만족
# (1 <= i < j <= n)
# 그리고 n이 100,000까지 가므로... 그냥 반복문 돌리면 큰일
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
# 투 포인터 => 이분탐색 style?
answer = 0
l, r = 0, n-1 # 인덱스 양 끝(왼쪽, 오른쪽)
while l < r:
    tmp = arr[l] + arr[r]
    # 합이 x면 답안 갯수 증가, 다음 l 확인
    if tmp == x:
        answer += 1
        l += 1
    # x보다 작다면 l을 증가시켜 더 큰 값 더하기
    elif tmp < x:
        l += 1
    else:
        r -= 1
print(answer)