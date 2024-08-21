# result1 = solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
# result2 = solution(5, [[1,1,0,1,0], [1, 1, 0, 0, 0], [0,0,1,0,1], [1,0,0,1,1], [0,0,1,1,1]])
#
# result1=4
# result2=1
# 입력값 〉 4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
# 기댓값 〉 1
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * (n + 1)
    check = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if computers[i - 1][j - 1] == 1 and i != j:
                check[i].append(j)

    if all(len(sublist) == 0 for sublist in check):
        return n

    # print(check)
    def bfs(check, start):
        q = deque()
        q.append(start)
        visited[start] = True

        while q:
            x = q.popleft()
            for k in check[x]:
                if not visited[k]:
                    visited[k] = True
                    q.append(k)

    for i in range(n):
        if check[i] and not visited[i]:
            bfs(check, i)
            answer += 1

    # print(visited)
    for i in visited[1:]:
        if not i:
            answer += 1

    return answer

print(solution(4, [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))
