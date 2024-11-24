
import heapq

def solution(operations):
    answer = []
    for i in operations:
        order, num = i.split(" ")
        
        # 삽입
        if order == "I":
            heapq.heappush(answer, int(num))
        
        # 최솟값 삭제
        elif order == "D" and num == "-1":
            if len(answer) < 1:
                continue
            else:
                heapq.heappop(answer)
                
        # 최댓값 삭제
        elif order == "D" and num == "1":
            if len(answer) < 1:
                continue
            else:
                answer.sort()
                answer.pop()
     
    if len(answer) == 0:
        return [0, 0]
    
    return [max(answer), min(answer)]