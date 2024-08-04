# 실버 3. 다음 순열
import sys, itertools
input = sys.stdin.readline
n = int(input())
perm = list(map(int, input().split()))

def next_perm(perm):
    n = len(perm)

    # 뒤에서부터 확인하며 오름차순이 깨지는 숫자 위치의 인덱스 찾기
    i = n-1
    while i > 0 and perm[i-1] >= perm[i]:
        i -= 1

    # 오름차순이 깨지지 않는다면 사전 순으로 마지막 순열
    if i <= 0:
        return False

    # 오름차순이 깨진 영역의 숫자 다음 숫자(더 큰 숫자)를 찾기
    j = n - 1
    while perm[j] <= perm[i-1]:
        j -= 1
    # 두 자리의 숫자 교환
    perm[i-1], perm[j] = perm[j], perm[i-1]

    #  i부터 끝까지의 순열 뒤집기
    perm[i:] = reversed(perm[i:])
    return  True

if next_perm(perm):
    print(' '.join(map(str, perm)))
else:
    print(-1)