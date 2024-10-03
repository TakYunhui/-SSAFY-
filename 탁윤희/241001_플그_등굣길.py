def solution(m, n, puddles):
    # m x n의 좌표지도, 물이 잠긴 지역 puddles

    # dp[i, j] = 좌표(i, j)에 도달하는 최단 거리(정수)를 저장, 갱신
    dp = [[0] * m for _ in range(n)]
    # 시작점 1로 초기화
    dp[0][0] = 1

    # 시간 효율성을 위해 puddles를 set 형태로 변경
    # 이때, 첫번째가 세로열 값이고 두번째가 가로열 값이다
    puddles = set((y - 1, x - 1) for x, y in puddles)
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0) or (i, j) in puddles:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007
    print(dp)

    return dp[n - 1][m - 1]