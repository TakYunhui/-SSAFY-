# 실버 3. 조합
# itertools combination: 모든 조합 직접 생성하고 순회
# math.comb 조합 수학적 공식으로 바로 계산
import math
n, m = map(int, input().split())
cnt = math.comb(n, m)
print(cnt)
