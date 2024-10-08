# 프로그래머스 2. 행렬의 곱셈
def solution(arr1, arr2):
    # 행렬 계산 : answer[i][j] = arr1[i] * arr2[j] 의 합산
    answer = [[0 for _ in range(len(arr2[0])) ] for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer