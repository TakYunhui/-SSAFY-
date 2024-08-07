import sys

sys.stdin = open('input.txt')

# 총 N일 하루에 K만큼 근손실

N, K = map(int, input().split(' '))
kits = list(map(int, input().split(' ')))

# 방문 표시를 위한 리스트
days = [0] * N
weight = 500
result = 0

# 재귀 함수로 정의
# x : 현재 중량, n : 날짜
def check(x, n):
    global result
    # 500보다 작아지면 실패
    if x < 500:
        return
    # 500보다 작지 않고 다 채우면
    if n == N:
        # 결과 추가
        result += 1
        return
    # 먼저 중량 빼고 시작
    x -= K
    for i in range(N):
        # 운동 체크 되어있지 않을 때
        if not days[i]:
            days[i] = 1
            # 재귀함수 돌리기
            check(x + kits[i], n+1)
            # 초기화
            days[i] = 0
check(500, 0)
print(result)