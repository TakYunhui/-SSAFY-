# 실버 2. 비슷한 단어 (복습)
# s = 'mississippi'
# d = defaultdict(int) - 기본값 정수 0 설정
# for k in s:
#     d[k] += 1
#
# sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
from collections import defaultdict
import sys
input = sys.stdin.readline


n = int(input())
words = []
for _ in range(n):
    word = input().strip()
    words.append(word)

pattern_dict = defaultdict(int)
for word in words:
    # 각 단어를 하나씩 순회하면서
    # mapping: dict를 이용해 단어 안 알파벳과 정수 매치
    # ㄴ mapping[char] == 0 일 때, 새 번호를 부여해야 하기에 그냥 dict() 사용
    # default(int) 쓰면 기존 값이 0 이라 무조건 1을 부여하게 되어서 안 됨
    # pattern: 위에서 최종 매치된 단어 정수들을 패턴 저장
    # => 단어 별로 새롭게 mapping, pattern 부여해야 같은 패턴을 같은 숫자로 매핑 가능
    # 따라서 각 단어를 순회할 때마다 초기화!
    mapping = {}
    pattern = []
    number = 1
    for char in word:
        if char not in mapping:
            mapping[char] = number
            number += 1
        pattern.append(mapping[char])
    pattern_dict[tuple(pattern)] += 1

# 같은 패턴을 가진 단어쌍 개수 계산
result = 0
for count in pattern_dict.values():
    if count > 1:
        result += count * (count - 1) // 2  # 조합 공식 nC2

print(result)