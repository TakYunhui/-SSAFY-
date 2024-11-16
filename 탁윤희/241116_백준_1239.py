# 골드 5. 차트
'''
10 40 10 40 - 2
10 50 40    - 1
50 50       - 1
1 48 1 1 48 1  - 3
2 2 96      - 0
'''
# 처음에 요소 개수에 따라 나눠져서 값이 구해지나 했다
# 하지만 같은 수를 가져도 값 비율에 따라 선의 수가 달라진다
# 원을 2등분 하는 선에 대한 기준을 찾아야 한다
# ==> 부분 집합의 합이 정확히 전체 합의 절반(50)이 되어야 함
# ==> 부분 집합 조합을 만들고 조합 안에 쓰인 반의 개수가 최대 선의 개수
# key: (1) 조합 구현 (2) 이미 쓰인 항목은 또 쓰이지 않게 하기 (visited 이용?)
# 근데 생각해보니 가장 많은 선이 되는 걸 답으로 채택하면 나머지 값은 안 봐도 됨 (자동으로 같은 수의 반이 쓰인 조합이 남을 것)
# (2)는 안 해도 될듯

# 2. 풀이참고
import sys
import itertools

def check(lst):
    line = []
    c = 0
    ans = 0
    for i in lst:
        c += i
        line.append(c)
    for i in range(0,len(line)-1):
        for t in range(i+1,len(line)):
            if line[i] + 50 == line[t]:
                ans += 1
    return ans

ans = 0
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split(" ")))
s.sort()
if max(s) > 50:
    print(0)
else:
    brt = list(itertools.permutations(s))
    for i in brt:
        ch = check(list(i))
        if ch > ans:
            ans = ch
    print(ans)

# 재귀로 조합 구현 => 순서는 중요하지 않으니 순열 대신 조합 !
# from itertools import combinations
#
# n = int(input())
# dogs = list(map(int, input().split()))
# def comb(arr):
#     max_len = 0
#     # 1부터 arr 길이까지 가능한 모든 조합 수 확인
#     for i in range(1, len(arr) + 1):
#         for j in combinations(arr, i):
#             print(j, len(j), sum(j))
#              => 이거 고쳐쓰려면 단일 요소가 50이상인 걸 뺀 다음
#                 50이 되는 조합의 대칭 쌍도 확인해야 함 -> 이게 어렵다
#             if len(j) != 1 and sum(j) == 50:
#                 max_len = max(max_len, len(j))
#     return max_len
#
# print(comb(dogs))

# ==> 부분집합의 합이 50인 것 중 가장 긴 것만 찾아서 예제2에서 2가 나온다
# => 50이 2개 나오는 세트를 찾고, 그들의 길이가 같아야지 선의 개수가 되는 듯?

# ==> 하나의 값이 50 이상이면 원을 나누지 못 한다! 이걸 고려 안 해서 틀림
