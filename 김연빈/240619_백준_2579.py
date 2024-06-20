# 계단 오르기
# 도착점은 무조건 밟기
# 한번에 하나 / 두계단
# 연속 세 계단 불가
# 시작점은 계단 아님
# 총 점수의 최댓값 출력

# dp 인것같은데 어떻게 하지? 배낭..그거인것 같기도 하고?
N = int(input())
step = [int(input()) for _ in range(N)]
step.insert(0, 0)

score = [0]*(N+1)

# 여기까지 오는데 걸린 최대합을 구한다.

# 계단이 2개 이하인 경우
if (N < 3) :
    print(sum(step))
else: # 3개 이상인 경우
    # 밟는 경우, 안밟는 경우 나눠서?
    # 마지막 계단을 무조건 밟아야하니까 마지막에서 내려가는 걸로? ㄴㄴ
    score[1] = step[1]
    score[2] = step[2] + score[1]
    for i in range(3, N+1):
        # 전칸을 밟고 이 칸을 밟는 경우
        tmp1 = score[i-3] + step[i-1] + step[i]
        # 전칸을 밟지않고 오는 경우
        tmp2 = score[i-2] + step[i]
        score[i] = max(tmp1, tmp2)
    print(score[N])

# print(score)
