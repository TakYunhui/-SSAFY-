def solution(brown, yellow):
    length = 3

    answer = []
    while length:
        # 갈색 가로가 length라면
        # 갈색 세로는?
        if (length - 2) * ((brown - (length * 2)) // 2) == yellow:
            answer = sorted([length, (brown - (length * 2)) // 2 + 2], reverse=True)
            return answer
        else:
            length += 1
        print(length)
    # return answer

brown = 24
yellow = 24

print(solution(brown, yellow))