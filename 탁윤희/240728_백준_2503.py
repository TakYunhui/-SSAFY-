# 실버3. 숫자 야구
# 숫자 제시 - 스트라이크 / 볼 개수
# 스트라이크 : 숫자 존재, 위치 같음
# 볼 : 숫자 존재, 위치 다름
# 전체 입력 끝나고 나올 수 있는 정답의 개수 출력
# 가능한 숫자 조합에서 안 되는 것들 제거
from itertools import permutations

n = int(input())
# 1~9의 숫자로 3가지 숫자 만들기
num_list = [str(i) for i in range(1, 10)]
all = list(permutations(num_list, 3))

for i in range(n):
    guess, strike ,ball = map(int, input().split())
    guess = list(str(guess)) # ['1', '2', '3']
    remove_cnt = 0
    # 가능성 없는 숫자 제거
    for i in range(len(all)):
        s, b = 0, 0
        i -= remove_cnt
        for j in range(3):
            # print(i, j , all[i][j], all[i], guess[j])
            if all[i][j] == guess[j]:
                s += 1
            elif guess[j] in all[i]:
                b += 1
        # 스트라이크나 볼 개수가 다르면 제거
        if s != strike or b != ball:
            all.remove(all[i])
            remove_cnt += 1

print(len(all))


