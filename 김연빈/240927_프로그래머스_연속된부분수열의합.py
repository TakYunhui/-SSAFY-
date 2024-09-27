# 비내림차순
# 부분 수열의 합은 k
# 길이가 짧은 수열, 앞쪽 수열


# 부분합?

seq = [1, 2, 3, 4, 5]
k = 7

# seq = [1, 1, 1, 2, 3, 4, 5]
# k = 5

# seq = [2, 2, 2, 2, 2]
# k = 6

def solution(sequence, k):
    answer = []
    n = len(sequence)
    sum_list = [0]*(n)
    sum_list[0] = sequence[0]
    point = -1
    start = n+2
    len_ans = n+2
    if sum_list[0] >= k:
        point = 0
    for i in range(1, n): # 부분합
        sum_list[i] = sum_list[i-1]+sequence[i]
        if point!=-1 and sum_list[i] >= k:
            point = i
    # print(sum_list)
    # 포인트부터 빼면서 찾기
    if sum_list[point] == k:
        answer = sequence[k:k+1]
    else:
        while point < n:
            for i in range(point):
                # 여기 조건을 잘 생각해보자
                if (sum_list[point]-sum_list[i])==k:
                    if (len_ans>n+1) or (point-i < len_ans):
                        if (start > n+1) or (start > i):
                            start = i
                            print(start)
                            len_ans = (point - i)
                            answer = [start, point]
            else:
                point += 1
    return answer

print(solution(seq, k))