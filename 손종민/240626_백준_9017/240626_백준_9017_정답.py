import sys

sys.stdin = open('input.txt')

from collections import Counter

# 테스트케이스
T = int(input())

for _ in range(T):
    N = int(input())
    rank = list(map(int, input().split(' ')))
    counter = Counter(rank)
    board = {}
    tmp = 0

    for i in range(N):
        # 해당 팀명 카운트 횟수가 6보다 작을 경우
        if counter[rank[i]] < 6:
            tmp += 1
            continue
        # 보드에 등록된 팀일 경우
        if rank[i] in board:
            # 탈락팀 제외한 값을 뺀 점수를 입력해주기
            board[rank[i]].append(i - tmp)
        # 등록되지 않은 팀이면
        else:
            # 팀 생성해주기
            board[rank[i]] = [i - tmp]
    # print(board)
    # 우선순위대로 정렬해주기
    print(sorted(board, key=lambda x:(sum(board[x][0:4]), board[x][4]))[0])