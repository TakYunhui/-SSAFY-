# 실버3. 교실 배정
# 반 배정 고려 x, 교실을 2개씩 짝짓는 방법 1가지 당 초코파이 1개
# => 시간초과남
from itertools import combinations
n = int(input())
# n개의 교실과 n/2개의 반
# 1. 교실 2개씩 짝 짓기
pairs = list(combinations(range(n), 2))
group_size = n // 2
result = []
print(pairs)
# 2. 교실 2개씩 짝 지은 걸 다시 조합으로 n//2 반에 맞게 맞춤
for group in combinations(pairs, group_size):
    used = set()
    for pair in group:
        used.update(pair) # 현재 pair 교실 번호를 set에 추가
    if len(used) == n: # 모든 교실이 중복 없이 사용되었다면
        result.append(group) # 그룹을 결과에 넣는다
print(result)