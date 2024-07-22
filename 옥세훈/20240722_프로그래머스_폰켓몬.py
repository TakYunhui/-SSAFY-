def solution(nums):
    answer = 0
    goal_num = len(nums) // 2
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    cnt = 0

    if len(dic) > goal_num:
        answer = goal_num
    else:
        answer = len(dic)

    return answer
