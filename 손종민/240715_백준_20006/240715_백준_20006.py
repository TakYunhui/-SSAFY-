import sys
sys.stdin = open('input.txt')



# p : 플레이어 수
# m : 정원
p, m = map(int, input().split())

roomlist = []
roomnum = 0
for _ in range(p):
    player = {}
    player['level'], player['name'] = input().split()
    # print(player)

    if len(roomlist) == 0:
        room = {}
        room['room_name'] = roomnum
        room['host'] = player
        room['member'] = []
        room['member'].append(player)
        roomlist.append(room)
        roomnum += 1
    
    else:
        isappended = False
        for room in roomlist:
            if -10 <= int(room['host']['level']) - int(player['level']) <= 10:
                if len(room['member']) < m:
                    room['member'].append(player)
                    isappended = True
                    break
        if isappended == False:
            room = {}
            room['room_name'] = roomnum
            room['host'] = player
            room['member'] = []
            room['member'].append(player)
            roomlist.append(room)
            roomnum += 1


for room in roomlist:
    if len(room['member']) == m:
        print('Started!')
    else:
        print('Waiting!')
    
    for player in sorted(room['member'], key=lambda x: x['name']):
        print(player['level'], player['name'])