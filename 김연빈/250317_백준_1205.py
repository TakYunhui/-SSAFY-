# 등수 구하기

N, score, P = map(int, input().split())
if (N==0):
    print(1)
else:
    score_list = list(map(int, input().split()))

    score_list.sort(reverse=True)
    new_list = score_list

    if (P > N):
        new_list = new_list + [0]

    if (score <= new_list[-1]):
        print(-1)
    else:
        for i in range(P):
            if (score >= new_list[i]):
                print(i+1)
                break