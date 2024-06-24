def solution(brown, yellow):
    answer = []

    # 가로, 세로 yellow를 가로가 더 길게 나눈뒤 + 2씩 해주면됨.
    for i in range(1, yellow + 1):
        for j in range(1, yellow + 1):

            if i < j:
                break
            if i * j == yellow:
                ni, nj = i + 2, j + 2
                if ni * nj == brown + yellow:
                    answer = [ni, nj]
                    print(answer)
                    return answer

    return answer

solution(18, 6)