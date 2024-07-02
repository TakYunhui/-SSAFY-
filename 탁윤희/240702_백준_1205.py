# 실버 4 - 등수 구하기
# 입력 : n - 현재 랭킹 개수, 새 점수, 랭킹에 들 수 있는 총 개수
# 같은 점수가 앞에 있으면 그 다음 ++ 점수됨
# 랭킹이 다 찼을 때는 새 점수가 이전 점수보다 좋을 때만 점수 변동
n, new, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
    scores.append(new)
    scores.sort(key=lambda x:-x)

    if len(scores) > p and scores[n] == new:
        print(-1)
    else:
        rank = 1
        for i in range(n+1):
            if scores[i] == new:
                print(rank)
                break
            else:
                rank += 1
else:
    print(1)