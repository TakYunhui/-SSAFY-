# 실버 1. 태권왕
# 수정점: check 배열이 필요 없어서 빠짐 -> 4ms 단축, 코드  길이 단축
from collections import deque
import sys
input = sys.stdin.readline

def bfs(mine, rival, cnt): # 현재 내 점수, 상대 점수, 누적 연속 발차기 횟수
    q = deque([(mine, rival, cnt)])
    while q:
        current_m, current_r, cumul_c = q.popleft()
        if current_m <= current_r:
            q.append((current_m + current_m, current_r + 3, cumul_c + 1))
            q.append((current_m + 1, current_r, cumul_c + 1))
            if current_m == current_r:
                return cumul_c

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t, 0))
