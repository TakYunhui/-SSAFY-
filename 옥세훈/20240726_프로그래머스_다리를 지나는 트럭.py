def solution(bridge_length, weight, truck_weights):
    answer = 0

    if bridge_length > len(truck_weights) and weight >= sum(truck_weights):
        answer = bridge_length + len(truck_weights)
        print(answer)
        return answer

    # if bridge_length > len(truck_weights) and weight < sum(truck_weights):

    # bridge_length씩 truck_weigths를 훑을거임
    for i in range(len(truck_weights) - bridge_length + 1):
        check = sum(truck_weights[i:i+bridge_length])
        print(truck_weights[i:i+bridge_length])
        if check >= weight:
            answer += bridge_length


    print(answer + len(truck_weights))
    return answer + len(truck_weights)

solution(10, 20, [10, 10, 10])