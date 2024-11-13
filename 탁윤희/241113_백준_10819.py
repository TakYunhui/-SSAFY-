# 실버2. 차이를 최대로
# n = int(input()) # 3 ~ 8
# arr = list(map(int, input().split()))
# visited = [0] * n
# result = 0
# # 수식에서 n-1번 값을 더하게 됨
# def cal(k, m, current_sum):
#     global result
#     if m == n-1:
#         result = max(result, current_sum)
#         return
#     else:
#         if k < n and not visited[k]:
#             visited[k] = 1
#             current_sum += abs(visited[k] - visited[k+1])
#             cal(k, m+1, current_sum)
#             visited[k] = 0
#
# cal(arr[0],0, 0)
# print(result)
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
result = 0


def backtrack(depth, prev_value, current_sum):
    global result
    # 모든 숫자를 사용한 경우 최대값 갱신
    if depth == n:
        result = max(result, current_sum)
        return

    # 가능한 숫자를 선택
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 숫자
            visited[i] = True
            if depth == 0:
                # 첫 숫자는 차이를 계산하지 않음
                backtrack(depth + 1, arr[i], current_sum)
            else:
                # 두 번째 숫자부터는 바로 절대값 차이를 누적
                new_sum = current_sum + abs(prev_value - arr[i])
                backtrack(depth + 1, arr[i], new_sum)
            visited[i] = False  # 백트래킹: 선택 취소


# 백트래킹 시작
backtrack(0, 0, 0)
print(result)
