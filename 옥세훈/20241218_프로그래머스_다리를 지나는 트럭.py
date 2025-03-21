from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    curWeight = 0
    while truck_weights:
        answer += 1
        
        curWeight = curWeight - bridge.popleft()
        
        # 현재 브릿지 무게 + 오는 트럭 무게 <= 제한 무게
        if curWeight + truck_weights[0] <= weight:
            curWeight = curWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())
            
        else:
            bridge.append(0)

        
              
    answer += len(bridge)
        
    return answer