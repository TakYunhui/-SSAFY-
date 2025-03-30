import sys
from collections import defaultdict

input = sys.stdin.readline
# 입력 받기
n = int(input().strip())  # 첫 줄: 수열 길이
arr = list(map(int, input().split()))  # 두 번째 줄: 수열 원소들

l, answer = 0, 0
count = defaultdict(int)  # 현재 윈도우에서 숫자별 개수 저장

for r in range(n):
    count[arr[r]] += 1  # 오른쪽 포인터 확장

    # 반석 조건을 만족할 때까지 l 증가
    while max(count) - min(count) > 2:
        count[arr[l]] -= 1
        if count[arr[l]] == 0:
            del count[arr[l]]  # 개수가 0이 되면 삭제
        l += 1  # 왼쪽 포인터 이동

    answer = max(answer, r - l + 1)  # 최대 길이 갱신

print(answer)
