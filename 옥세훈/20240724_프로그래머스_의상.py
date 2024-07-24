
def solution(clothes):
    answer = 1
    dic = {}

    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1

    for i in dic:
        answer *= (dic[i] + 1)
    print(answer - 1)
    return answer - 1

solution([["a", "A"], ["b", "B"], ["c", "C"], ["aa", "A"]])
#[["a", "A"], ["b", "B"], ["c", "C"]], 7