# 최솟값 만들기
# 작은수 * 큰 수의 합으로?
# 배열 정렬을 서로 반대로 하고 곱하기?


def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]


    return answer

A = [1,2]
B = [3, 4]

print(solution(A, B))