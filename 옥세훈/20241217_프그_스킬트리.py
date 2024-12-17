def solution(skill, skill_trees):
    answer = 0
    check = list(skill)

    dic = dict()
    for idx, c in enumerate(check):
        dic[c] = idx

    for i in skill_trees:
        ls = list(i)

        for x in range(len(check)):
            if check[x] in ls:
                break
            else:
                if x == len(check)-1:
                    answer += 1


        for j in range(len(ls)):
            h = ls[j]
            if h not in check:
                ls[j] = "0"
                # print(j, ls)

        new_str = ''.join(ls).replace("0", '')

        temp = -1
        flag = False
        check_num = []
        for k in new_str:
            if temp+1 == dic[k]:
                temp = dic[k]
                check_num.append(dic[k])
            else:
                flag = True
                break

        # print(check_num, i, "check")
        if flag:
            flag = False
            continue

        if check_num and check_num[0] == 0:
            # print(check_num, i, "OK")
            answer += 1


    return answer