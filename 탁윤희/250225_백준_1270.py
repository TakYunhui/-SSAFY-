# 실버 3. 전쟁 - 땅따먹기
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    soldiers = list(map(int, input().split()))
    half = len(soldiers) / 2

    military_state = dict()
    for soldier in soldiers:
        military_state[soldier] = military_state.get(soldier, 0) + 1

    # 가장 많이 등장한 병사 찾기
    max_soldier = max(military_state, key=military_state.get)

    # 절반보다 많은 경우 해당 병사 번호 출력
    if military_state[max_soldier] >= half:
        print(max_soldier)
    else:
        print("SYJKGW")

