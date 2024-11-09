def solution(numbers):
    answer = ''
    # 1. numbers 문자열로 변경
    numbers = [str(number) for number in numbers]
    # 2. numbers 순서대로 정렬
    # 문제에서 숫자는 최대 1000의 값을 가지므로 숫자를 3번 반복하면 3자리 이상의 문자열이 되어 비교할 수 있게 됨
    # 문자열에서 각 자리에서 더 큰 값이 나오면 그 값이 더 큰 문자열로 판별됨 ( 1번째 자리 수가 큰 값이 큰 값)
    numbers.sort(key = lambda x: x*3, reverse = True)

    return str(int(''.join(numbers)))