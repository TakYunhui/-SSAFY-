1
2
3
4
5
6
7
8
9
10
11
12
13
14
def solution(numbers):

    answer = [-1] * len(numbers)
    stack = [numbers[-1]]
    for i in range(len(numbers)-2, -1, -1):

        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])

    return answer
