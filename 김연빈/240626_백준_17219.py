# 비밀번호 찾기

N , M = map(int, input().split())

memo = dict()

for _ in range(N):
    address, pw = input().split()
    memo[address] = pw

for _ in range(M):
    find_add = input()
    print(memo[find_add])
