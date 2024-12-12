def solution(elements):
    answer = set()
    
    element_len = len(elements)
    elements = elements * 2
    # print(elements)
    
    for i in range(element_len):
        for j in range(element_len):
            answer.add(sum(elements[j:j+i+1]))
    
    return len(answer)