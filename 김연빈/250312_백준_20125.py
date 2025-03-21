# 쿠키의 신체 측정
N = int(input())
board = []
heart_x = 0 #행
heart_y = 0 #열
left_leg = 0
left_arm = 0
right_leg = 0
right_arm = 0
wrest = 0
for _ in range(N):
    board.append(list(input()))
for i in range(N):
    for j in range(N):
        if board[i][j]=='*':
            heart_x = i+1
            heart_y = j
            break
    if (heart_x>0):
        break

for j in range(heart_y):
    if (board[heart_x][j]=='*'):
        left_arm += 1
for j in range(heart_y+1, N):
    if (board[heart_x][j]=='*'):
        right_arm += 1
end_wrest = 0 # 다리시작
for i in range(heart_x+1, N):
    if (board[i][heart_y]=='_'):
        end_wrest = i
        break
    else:
        wrest += 1
for i in range(end_wrest, N):
    if (board[i][heart_y-1]=='*'):
        left_leg += 1
    else:
        break
for i in range(end_wrest, N):
    if (board[i][heart_y+1]=='*'):
        right_leg += 1
    else:
        break

print(heart_x+1, heart_y+1)
print(left_arm, right_arm, wrest, left_leg, right_leg)