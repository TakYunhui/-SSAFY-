def solution(phone_book):
    answer = True
    dict = {}
    for nums in phone_book:
        dict[nums] = 1
    
    for nums in phone_book:
        tmp = ""
        for num in nums:
            tmp += num
            
            if tmp in dict and tmp != nums:
                answer = False
            

    return answer