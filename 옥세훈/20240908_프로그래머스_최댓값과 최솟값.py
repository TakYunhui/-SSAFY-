def solution(s):
    answer = ''
    ls = []

    check = list(s.split())
    for i in check:
        ls.append(int(i))

    ls = sorted(ls)
    min = str(ls[0])
    max = str(ls[-1])
    answer = min + " " + max
    return answer