# 숫자를 문자열로 바꾸고
# for문 돌려서 각 자리 합하고
# 마지막 자리의 경우
# 6보다 크면 (10 - n) + 1 더해주기
# 6보다 작으면 n 더해주기


def solution(storey):
    answer = 0
    storey = str(storey)
    for i in range(len(storey)):
        if int(storey[i]) > 5:
            
            answer += (10 - int(storey[i]) + 1)
        else:
            answer += int(storey[i])
    return answer


storey = 16

print(solution(storey))