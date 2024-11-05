def solution(k, dungeons):
    global answer, visited
    answer = 0
    # 던전 방문 여부 체크 visited
    visited = [0 for _ in range(len(dungeons))]
    dfs(k, dungeons, 0)
    return answer


def dfs(k, dungeons, cnt):
    global answer
    # 최대 던전 수를 찾을 거니 answer보다 cnt가 크면 업데이트
    if cnt > answer:
        answer = cnt

        # 던전들 중에서
    for i in range(len(dungeons)):
        # 아직 방문하지 않았고, 필요 피로도보다 현재 소유 피로도 k가 크다면
        if not visited[i] and k >= dungeons[i][0]:
            # 던전 방문
            visited[i] = 1
            # 현재 피로도 - 소모 피로도, 던전 배열 , 던전 방문수 증가
            dfs(k - dungeons[i][1], dungeons, cnt + 1)
            visited[i] = 0