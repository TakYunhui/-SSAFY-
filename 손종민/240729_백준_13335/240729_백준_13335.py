import sys

sys.stdin = open('input.txt')

from collections import deque

n, w, L = map(int, input().split(' '))
trucks = deque(list(map(int, input().split(' '))))

# 트럭 하중 합을 위한 deque
truck_on_bridge = deque([0] * w)
time = 0
while truck_on_bridge:
    time += 1
    truck_on_bridge.popleft()
    if trucks:
        if sum(truck_on_bridge) + trucks[0] <= L:
            truck_on_bridge.append(trucks.popleft())
        else:
            truck_on_bridge.append(0)

    # 다리 위에 있는 트럭 하중 합이 다리 하중 합보다 작으면
    # if sum(truck_on_bridge) <= L:
    #     if not trucks:
    #         time += w
    # else:
    #     time += w
    #     truck_on_bridge.popleft()

print(time)