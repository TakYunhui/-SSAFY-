t = int(input())
for _ in range(t):
    result = "YES"
    n = int(input())
    # 전화번호를 문자열 채로 받는다 - int로 받으면 반복문에서 startswith method로 확인 불가
    numbers = list(input() for _ in range(n))
    numbers.sort()

    for i in range(n - 1):
        if numbers[i + 1].startswith(numbers[i]):
            result = "NO"
            break # 일관성 하나라도 없게 되면 바로 NO로 만든 후, 순회 종료
    print(result)
