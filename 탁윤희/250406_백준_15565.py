# 실버 1. 귀여운 라이언
n, k = map(int, input().split())
dolls = list(map(int, input().split()))
# 라이언 인형 k 개 있는 가장 작은 연속된 인형 집합
# 라이언 : 1 , 어피치 : 2
answer = int(1e9) # 집합 갯수 최소로 저장할 것
l, r = 0, 0
lions = 0

if dolls[r] == 1:
    lions += 1

while l <= r and r < n:
    # 라이언이 k개면 answer 갱신
    # r - l + 1 인덱스로 인형 집합 크기 계산
    if lions == k:
        answer = min(answer, r - l + 1)
        # 시작 인덱스 인형이 라이언이면 이걸 제거하고, 시작 인덱스 1 추가
        if dolls[l] == 1:
            lions -= 1
        l += 1
    # 라이언이 k개 이하면 끝 인덱스 1 추가해서 다음 인형 확인한다
    else:
        # 만약 추가된 r 인덱스의 인형이 라이언이면 라이언 추가함
        r += 1
        if r < n and dolls[r] == 1:
            lions += 1

if answer == int(1e9):
    print(-1)
else:
    print(answer)