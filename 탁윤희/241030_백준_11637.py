# 실버 5. 인기투표
t = int(input())
# 테스트 케이스 동안 진행
for _ in range(t):
    n = int(input()) # 후보자 수
    # (후보자 번호, 후보자 득표수) 튜플 형태로 리스트에 저장
    votes = list((i+1, int(input())) for i in range(n))
    # 과반수 = 총 득표수 // 2
    total_votes = 0
    maximum_votes = 0
    maximum_cnt = 1
    for i in range(n):
        # 누적 득표수 구하는 값
        total_votes += votes[i][1]
        # 최대 득표수가 또 있으면 득표자 수 늘림
        if maximum_votes == votes[i][1]:
            maximum_cnt += 1
        else:
            maximum_cnt = 1
        # 최대 득표수 갱신
        maximum_votes = max(maximum_votes, votes[i][1])

    majority = total_votes // 2
    if maximum_cnt > 1:
        print("no winner")
    else:
        # 득표수 기준 내림차순 정렬
        votes.sort(key=lambda x:x[1], reverse=True)
        if maximum_votes > majority:
            print(f"majority winner {votes[0][0]}")
        else:
            print(f"minority winner {votes[0][0]}")
