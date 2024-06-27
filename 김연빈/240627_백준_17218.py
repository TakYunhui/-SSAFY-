# 비밀번호 만들기

# 문자열 최대 40글자니까 브루트포스? 아닌가 너무 경우의 수가 많을지도
# 가장 긴 공통된 문자열 찾기

# 마지막까지 갔을때 가장 긴 문자열로?
# 앞에꺼중에 가장 긴 문자열 개수 +1
# 못풀겠다.
pw1 = input()
pw2 = input()

ans_list = [''] * len(pw1)
check = [[0] * len(pw1), [''] * len(pw1)]
print(check)

for i in range(len(pw2)):
    for j in range(len(pw1)):
        if (pw2[i] == pw1[j] and check[0][j] == 0):
            if (j == 0):
                max_index = 0
            else:
                max_index = check[0].index(max(check[0][:j]))
            check[0][j] = check[0][max_index] + 1
            check[1][j] = check[1][max_index] + pw1[j]

print(check)


