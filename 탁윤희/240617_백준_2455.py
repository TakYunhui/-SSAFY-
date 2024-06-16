# 브론즈 3 : 지능형 기차

result = 0
for i in range(4):
    embark, board = map(int, input().split())

    if embark == 0:
        current_passengers = board
    elif board == 0:
        result = max(result, current_passengers)

    else:
        passengers = current_passengers
        current_passengers = passengers - embark + board
        result = max(passengers, current_passengers)

print(result)