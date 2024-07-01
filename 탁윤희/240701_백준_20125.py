# 실버 4. 쿠키의 신체 측정
# 맨왼쪽 위 칸 (1,1) 오른쪽 아래 칸(n,n)
# 머리: 심장 위 1칸(-1, 0), 팔: 심장 왼쪽(0, -1), 오른쪽(0, +1)
# 허리: 심장 아래, 다리: 허리 왼쪽 아래(+1, -1), 오른쪽 아래(+1, +1)
# 심장 위치, 팔, 다리, 허리 길이 구하기
# 심장 -> 상하좌우 모두 *이 존재하는 것
# 무조건 머리부터 나옴 -> 처음 나온 *는 머리, 그 아래가 심장
# 나머지는 심장 기준으로 계산해서 구하면 됨!
n = int(input())
# 2차원 배열(문자 배열) 받기
arr = [list(input()) for _ in range(n)]

# 심장 위치와 신체 부위 길이 초기화
check, left, right = 0, 0, 0
left_arm, right_arm, waist, left_leg, right_leg = 0, 0, 0, 0, 0

for i in range(n):
    for j in range(n):
        # 심장 위치 찾기
        if not check and arr[i][j] == "*":
            check = [i+1, j]
            print(check[0] + 1, check[1] + 1)  # 심장 위치 출력

        # 심장 위치 기준으로 신체 부위 길이 계산
        if check and i == check[0] and j == check[1]:
            # 왼팔 구하기
            temp_j = j
            while temp_j > 0 and arr[i][temp_j-1] == "*":
                temp_j -= 1
                left_arm += 1

            # 오른팔 구하기
            temp_j = j
            while temp_j+1 < n and arr[i][temp_j+1] == "*":
                temp_j += 1
                right_arm += 1

            # 허리 구하기
            temp_i = i
            while temp_i+1 < n and arr[temp_i+1][j] == "*":
                temp_i += 1
                waist += 1

            # 허리 끝난 후 다리 시작
            # 왼다리 구하기
            left_i, left_j = temp_i + 1, j - 1
            while left_i < n and left_j >= 0 and arr[left_i][left_j] == "*":
                left_leg += 1
                left_i += 1

            # 오른다리 구하기
            right_i, right_j = temp_i + 1, j + 1
            while right_i < n and right_j < n and arr[right_i][right_j] == "*":
                right_leg += 1
                right_i += 1
            break  # 모든 계산이 끝나면 이중 루프 탈출

print(left_arm, right_arm, waist, left_leg, right_leg)