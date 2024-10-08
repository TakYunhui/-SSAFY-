def solution(want, number, discount):
    answer = 0
    len_dis = len(discount)
    len_want = len(want)

    # print(len_dis)
    flag = False
    # 10개씩 슬라이스 후 일일이 카운트?
    for i in range(len_dis - 9):
        check_ls = discount[i:i + 10]

        for j in range(len_want):
            num = number[j]
            stuff = want[j]
            check_num = check_ls.count(stuff)

            if check_num == num:
                flag = True
                continue
            else:
                flag = False
                break

        if flag:
            answer += 1
ㅎ
    return answer