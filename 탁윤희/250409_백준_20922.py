# 실버 1. 겹치는 건 싫어
from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))
# 인덱스 시작, 끝, 같은 정수 개수
# 최장 연속 부분 수열 길이 => 연속: 증가, 감소 개념이 아니고 그냥 붙어있는 연속
l, r = 0, 0
# 정수를 dict 로 관리해야 할 듯?
cnt = defaultdict(int)
answer = 0
while l <= r and r < n:
    # 현재 key의 value +1 이 k개가 안 되면
    # dict에 현재 정수 개수 추가하고 오른쪽으로 이동시켜서 배열 증가시킴
    if cnt[arr[r]] + 1 <= k:
        cnt[arr[r]] += 1
        # answer 갱신
        answer = max(answer, r - l + 1)
        # r을 제일 마지막에 증가시켜야 올바른 answer 값 갱신 가능
        r += 1
    else:
        cnt[arr[l]] -= 1
        l += 1

print(answer)
