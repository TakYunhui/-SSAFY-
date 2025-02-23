# 실버2. 비슷한 단어
# 비슷한 단어 쌍?
# 비슷하다: 임의의 알파벳을 바꾼다, 두 개의 다른 알파벳을 하나의 알파벳으로 바꾸는 건 안된다
# 숌스럽게 비슷하다: 모든 알파벳 -> 다른 알파벳, 알파벳 순서는 변경 x
# => 각 단어를 패턴화시키고, 패턴에서 나오는 비슷한 경우의 수 조합 구하기
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

# 패턴별로 그룹화 : defaultdict - 키가 존재하지 않을 때 기본값 설정(정수형은 0)
pattern_count = defaultdict(int)

for word in words:
    mapping = {}
    pattern = []
    current_number = 1
    # 단어 안의 알파벳을 출현 순서 대로 숫자와 매핑
    for char in word:
        # 아직 매핑되지 않았다면 숫자 부여
        if char not in mapping:
            mapping[char] = current_number
            current_number += 1
        # 매핑 되었다면 기존 숫자 사용해서 패턴에 추가
        pattern.append(mapping[char])
    # 패턴을 튜플로 변환하여 사용
    # 패턴 별 등장 횟수 집계
    print(pattern,mapping)
    pattern_count[tuple(pattern)] += 1
print(pattern_count)

# 같은 패턴을 가진 단어쌍 개수 계산
result = 0
for count in pattern_count.values():
    if count > 1:
        result += count * (count - 1) // 2  # 조합 공식 nC2

print(result)