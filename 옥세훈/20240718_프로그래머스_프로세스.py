def solution(priorities, location):
    answer = 0
    check_ls = [i for i in range(1, len(priorities) + 1)]
    q = priorities

    while q:
        check = q.pop(0)
        check_idx = check_ls.pop(0)

        print(check, " a")
        print(check_idx, "b")


        if len(q) > 1 and check < max(q):
            q.append(check)
            check_ls.append(check_idx)
        else:
            answer += 1
            if check_idx == location + 1:
                print(answer)
                break

        print(answer, "c")
    return answer

solution([2, 1, 3, 2], 2)