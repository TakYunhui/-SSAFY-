from itertools import combinations, permutations


def solution(k, dungeons):
    answer = 0
    check_ls = permutations(dungeons, len(dungeons))
    result_ls = []

    for i in check_ls:
        check_num = 0
        current_k = k
        for j in i:
            if j[0] <= current_k:
                current_k = current_k - j[1]
                check_num += 1
        result_ls.append(check_num)

    answer = max(result_ls)
    return answer

solution(80, [[80,20],[50,40],[30,10]])