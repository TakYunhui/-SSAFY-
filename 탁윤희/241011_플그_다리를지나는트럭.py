from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0  # 경과 시간
    waiting = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 다리위 트럭 상태 - length개 까지만 올라갈 수 있다 + 0으로 빈 공간 표현
    # 트럭이 한 칸씩 이동하게 됨~
    total_weight = 0  # 다리 위 트럭 무게

    while bridge:
        # 매 초, 가장 앞에 있는 트럭 이동
        answer += 1
        moving_truck = bridge.popleft()
        total_weight -= moving_truck
        # 다음 트럭을 위에 올릴 수 있는지 확인
        if waiting:
            if total_weight + waiting[0] <= weight:
                next_truck = waiting.popleft()
                bridge.append(next_truck)
                total_weight += next_truck
            else:
                # 무게 초과면
                bridge.append(0)

    return answer