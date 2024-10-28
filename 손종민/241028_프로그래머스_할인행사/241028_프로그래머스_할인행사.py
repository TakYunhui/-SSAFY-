# 딕셔너리에 want:number로 정리한다음에
# 0부터 len(discount) - 19 - 1 까지 range에서
# 카운트한 갯수와 딕셔너리 각 갯수가 일치하면
# 해당 일자 프린트 (인덱스 + 1)

from collections import defaultdict, Counter

def solution(want, number, discount):
    products = defaultdict()
    count = 0
    for i in range(len(want)):
        products[want[i]] = number[i]
    
    # print(products)
    isFound = False
    for i in range(0, len(discount) - 9):
        tmp = Counter(discount[i:i+10])
        # print(tmp)
        if tmp == products:
            isFound = True
            count += 1
        
    if isFound == False:
        return 0
    else: return count


want = ["banana", "apple", "rice", "pork", "pot"]


number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))