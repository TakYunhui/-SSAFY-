def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ls = []
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):
                a += arr1[i][k] * arr2[k][j]
                # print(arr2[k][j], k, j)
            ls.append(a)
        answer.append(ls)

    return answer