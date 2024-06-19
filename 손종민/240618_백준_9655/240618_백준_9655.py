# 9655 돌 게임

# 돌 1개 or 3개씩 가져가고, 마지막 돌 가져가는 사람이 이김
# N에서 1~3씩 빼고 0이 되면 이김
# SK부터 시작, 

N = int(input())
count = 0

while N > 0:
    count += 1
    if N >= 3:
        N -= 3
    elif N < 3:
        N -= 1

    
if count % 2 == 1:
    print('SK')
else:
    print('CY')