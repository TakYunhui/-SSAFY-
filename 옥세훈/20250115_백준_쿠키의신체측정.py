# 1. 심장부터 찾아보자
n = int(input())
arr = [list(input()) for i in range(n)]
heart_i, heart_j, r_arm, l_arm, waist, r_leg, l_leg = 0, 0, 0, 0, 0, 0, 0

flag = False
# 심장찾기
for i in range(n):
    if flag:
        break
    for j in range(n):
        if arr[i][j] == '*':
            cnt = 0
            ni = i
            while ni > -1:
                ni -= 1
                # 위로가자
                if cnt > 1 or arr[ni][j] != '*':
                    break

                if arr[ni][j] == '*':
                    cnt += 1

            if cnt == 1:
                heart_i, heart_j = i, j
                flag = True
                break

# 마지막에 1씩 더해줘야함, 문제에서는 1,1 시작이라 되어있기 때문
print(heart_i+1, heart_j+1)

# 왼쪽 팔
l_arm_idx = heart_j
while l_arm_idx > 0:
    l_arm_idx -= 1

    if arr[heart_i][l_arm_idx] != "*":
        break
    else:
        l_arm += 1

# 오른쪽 팔
r_arm_idx = heart_j
while r_arm_idx < n-1:
    r_arm_idx += 1

    if arr[heart_i][r_arm_idx] != "*":
        break
    else:
        r_arm += 1


# 허리
waist_idx = heart_i
check_leg_i = 0
while waist_idx < n:
    waist_idx += 1

    if arr[waist_idx][heart_j] != "*":
        check_leg_i = waist_idx-1
        break
    else:
        waist += 1

# 왼쪽 다리
l_leg_i, l_leg_j = check_leg_i, heart_j - 1
while l_leg_i < n-1:
     l_leg_i += 1

     if arr[l_leg_i][l_leg_j] != "*":
         break
     else:
         l_leg += 1

 # 오른쪽 다리
r_leg_i, r_leg_j = check_leg_i, heart_j + 1
while r_leg_i < n-1:
     r_leg_i += 1

     if arr[r_leg_i][r_leg_j] != "*":
         break
     else:
         r_leg += 1

print(l_arm, r_arm, waist, l_leg, r_leg)