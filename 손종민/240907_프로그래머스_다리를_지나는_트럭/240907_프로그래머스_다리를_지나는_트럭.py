def solution(bridge_length, weight, truck_weights):
    answer = 0
    checker = len(truck_weights)
    finished = []
    on_the_bridge = []
    time = 0
    while truck_weights:
        # 트럭 출발시키기
        this_truck = truck_weights.pop(0)
        # 현재 다리 위에 트럭이 없으면
        if not on_the_bridge:
            # 다리 위에 올리기
            on_the_bridge.append(this_truck)
            answer += 1
        # 다리 위에 트럭이 있고, 다리 위 위트럭과 현재 트럭 무게 합이 초과하는 경우
        # 대기하게 만들어야 함    
        elif on_the_bridge and sum(on_the_bridge) + this_truck > weight:
            answer += bridge_length
            finished.append(on_the_bridge.pop(0))
            # 한 대 보내고 남아있을 경우
            while on_the_bridge:
                finished.append(on_the_bridge.pop(0))
                answer += 1
            on_the_bridge.append(this_truck)
            answer += 1
        elif on_the_bridge and sum(on_the_bridge) + this_truck <= weight:
            on_the_bridge.append(this_truck)
        print('다리를 지난 트럭 :', finished)
        print('다리를 건너는 트럭 :', on_the_bridge)
        print('대기 트럭 :', truck_weights)
        print('경과 시간 :', answer)
    
    if on_the_bridge:
        answer += bridge_length

    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))