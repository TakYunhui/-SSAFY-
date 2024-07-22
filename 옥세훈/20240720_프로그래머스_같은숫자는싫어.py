def solution(arr):
    answer = []
    leng = len(arr)

    for i in range(leng-1):
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    answer.append(arr[-1])

    return answer

solution([4,4,4,3,3])