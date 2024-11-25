def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    isOkay = True
    for i in range(len(skill_trees)):

        tmp = []
        this_tree = list(skill_trees[i])
        for j in range(len(this_tree)):
            if this_tree[j] in skill:
                tmp.append(this_tree[j])
        if skill == tmp:
            print('일치하는 경우')
            answer += 1
        elif tmp in skill:
            print('포함된 경우')
            answer += 1
        # for k in range(len(tmp)):
        #     if k > 0 and tmp[k] < tmp[k - 1]:
        #         isOkay = False
        #         break
        # if isOkay == True:
        #     answer += 1

    return answer


skill = 'CBD'
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']

print(solution(skill, skill_trees))