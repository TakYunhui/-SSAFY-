# 실버 1. 숫자놀이
n = int(input()) # 사용하는 정수 수
integers = list(map(int, input().split())) # 크기 순으로 주어지는 정수들
k = int(input()) # 정수 사용 최대 횟수
# 홀수 - 짝수 순으로 상대보다 1 큰 정수를 만들어야 한다, 숫자 못 만들면 패배
# 정수를 최대 k번 사용할 수 있으므로 정수 중 가장 큰 수 x k로 dp 설정
max_num = k * max(integers)
dp = [(k+1) for _ in range(max_num)]
# 첫 시작은 0
dp[0] = 0

# dp[i] = i를 만드는 데 필요한 횟수 cnt
for i in range(1, max_num):

    for num in integers:
        if i >= num:
            # 현재 dp[i]와 현재 숫자 i에서 num 뺀 dp에 든 cnt 값 + 1 을 비교
            dp[i] = min(dp[i], dp[i-num] + 1)

# dp[i]가 k 초과하면 정답 출력
for i in range(1, max_num):
    if dp[i] > k:
        if i % 2:
            print(f"jjaksoon win at {i}")
        else:
            print(f"holsoon win at {i}")
        break # 처음으로 만족하는 숫자를 찾으면 루프 종료, break가 없으면 끝까지 실행됨
