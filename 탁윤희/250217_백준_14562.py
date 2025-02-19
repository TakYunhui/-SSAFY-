# 실버 1. 태권왕
# 수정점: check 배열이 필요 없어서 빠짐 -> 4ms 단축, 코드  길이 단축
from collections import deque
import sys
input = sys.stdin.readline

def bfs(mine, rival, cnt):
    q = deque([(mine, rival, cnt)])
    while q:
        m, r, now = q.popleft()

        if m <= r: # 현재 내 점수가 상대보다 작을 때 (왜 작을 때 한정? 값을 키우는 작업만 하기 때문)
            q.append((m+m, r+3, now+1))
            q.append((m+1, r, now+1))
            if m == r:
                return now

c = int(input())
for _ in range(c):
    s, t = map(int, input().split())
    print(bfs(s, t, 0))