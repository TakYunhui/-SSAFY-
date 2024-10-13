def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        # 확인하지 않은 컴퓨터라면
        if not visited[i]:
            # stack을 통한 dfs 과정
            stack = [i]
            while stack:
                now = stack.pop()
                if not visited[now]:
                    visited[now] = 1
                    # next: 다음 컴퓨터 번호, 배열 안의 컴퓨터 번호로 생각하면 된다
                    for next in range(n):
                        if computers[now][next] == 1 and not visited[next]:
                            stack.append(next)
                        # print(next, now, computers[now][next], stack)
            # while문이 끝나면서 하나의 네트워크를 완전히 탐색한 상태, 네트워크 개수 추가
            answer += 1
            # print(answer)

    return answer