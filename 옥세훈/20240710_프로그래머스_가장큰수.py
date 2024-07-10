def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'

    ls = []
    for i in numbers:
        ls.append(str(i))

    new_ls = sorted(ls, key=lambda x: x * 10, reverse=True)

    for i in new_ls:
        answer += i

    return answer

# 첫번째 생각은 각 배열을 문자열로 변환하여 각 인자의 첫번쨰 부분만 정수로 형변환한 후 크기대로 정렬하고자 했다.
# 그러나 34, 30 과 같은 수들이 있을때 34가 먼저 와야 함을 깨달았고, 이를 반영하고자 , 인자값에 * 10 을 해주는 것이다.
# 이는 숫자가 아니기 떄문에 343434... 이런식으로 나오는데 이를 ASCII 값으로도 크기를 비교할 수 있다는 것을 깨달았다.
# 전체 크기를 비교하는 것이 아니라, 첫 번쨰 문자부터 차례로 비교한다 즉 9와 34를 비교하는데 9 와 3을 비교하면서 전자가 더 크다고 판단하는 것이다.