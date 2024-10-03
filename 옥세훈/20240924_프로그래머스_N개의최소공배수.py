# [100, 99, 98, 97, 96] -> 376437600

def solution(arr):
    answer = 1
    arr.sort()

    check = arr[0]
    for i in range(1, len(arr)):
        if arr[i] % check == 0:
            arr[i] = arr[i] / check

    for i in range(len(arr)):
        answer *= arr[i]
    print(answer)
    return answer

solution([100, 99, 98, 97, 96])