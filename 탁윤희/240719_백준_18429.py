# 실버3. 근손실
# 모든 날짜가 중량을 500 이상으로 유지하는 경우의 수 구하기
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
kits = list(map(int, input().rstrip().split()))

def back(cnt, weight):
    global result
    if cnt == n:
        result += 1
        return
    if weight < 500:
        return
    weight -= k
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            # 운동하는 걸 적용 시킨다면 횟수 + 1, 중량 + 
            back(cnt + 1, weight + kits[i])
            visited[i] = 0

result = 0
visited = [0] * n
back(0, 500)
print(result)