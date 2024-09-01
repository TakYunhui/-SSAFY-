# 실버1. 캡틴 이다솜

n = int(input())

arr = []
num = 0
i = 1
# 사면체 만드는 데 쓰는 대포알 개수 list에 저장
while n > num:
    num += (i * (i+1)) // 2 # 사면체에 들어가는 대포알 수 계산식
    arr.append(num)
    i += 1

dp = [int(1e9) for _ in range(n+1)]
# 대포알 개수에 대한 최소 사면체 개수 계산
for j in range(1, n+1):
    # arr에 저장된 대포알 개수 num 탐색 - 사면체 하나에 들어가는 대포알 수
    for num in arr:
        # 대포알로 정확히 하나의 사면체를 만들 수 있음 - 더 탐색할 필요 없으므로 종료
        if num == j:
            dp[j] = 1
            break
        # num이 j보다 크면 현재 사면체 대포알 수를 초과하니 루프 종료
        elif num > j:
            break
        # 현재 j에서 num을 뺄 때 남은 대포알 개수인 j-num에서
        # 최소 사면체 개수를 구한 값에 1(현재 사면체 1개 생성)을 더해 현재 j의 최소 사면체 개수 갱신
        dp[j] = min(dp[j], 1+dp[j-num])

print(dp[n])