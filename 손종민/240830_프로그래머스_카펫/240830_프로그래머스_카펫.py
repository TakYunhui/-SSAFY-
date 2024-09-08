# 갈색 수, 노랑 수 주어짐
# 갈색은 무조건 테두리를 차지해야 함.
# 가로보다 세로가 무조건 길다.

# 10, 2의 경우
# 경우의 수
# 둘의 합 12
# 세로가 3 이상일 수밖에 없으므로
# 음... 모르겠다;;


def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if 2*yellow_x + 2*yellow_y + 4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                break 
            answer.sort(reverse = True)
    return answer
