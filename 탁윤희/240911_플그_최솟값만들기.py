# 레벨2.최솟값 만들기
def solution(A, B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort(reverse=True)
    print(A, B)
    for i in range(n):
        answer += A[i] * B[i]

    return answer