


def solution(numbers):
    # 문자열로 변환
    sorted(numbers, reverse=True)
    tmp = []
    for number in numbers:
        tmp.append(str(number))

    # 문자열에서의 대소 비교는
    # 아스키 코드로 비교
    # 따라서 원소가 1000 미만이므로, 다 세자리로 바꿔서 비교
    tmp.sort(key=lambda x: x*3, reverse=True)
    # print(tmp)
    answer = ''
    for num in tmp:
        answer += num
    return str(int(answer))


numbers = [3, 30, 34, 5, 9]


print(solution(numbers))