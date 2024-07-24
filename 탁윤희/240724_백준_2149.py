# 실버 3. 암호 해독
# 키를 기준으로 정렬
key = list(input())
pwd = list(input())
# key를 알파벳 순서로 정렬, 해당 열 문자 리스트, 사용 여부
arr = [[c, [], False] for c in sorted(key)]

# 암호문을 키 길이 기준으로 나누어 열로 정렬
for i in range(len(pwd)):
    arr[i // (len(pwd) // len(key))][1].append(pwd[i])

ans = []
# 원래 키 순서대로 재정렬, arr[i][2] boolean값으로 중복 추가 방지 - 같은 문자 순서 맞추기
for c in key:
    for i in range(len(arr)):
        if c == arr[i][0] and arr[i][2] is False:
            arr[i][2] = True
            ans.append(arr[i][1])
            break

for i in range(len(ans[0])):
    for j in range(len(ans)):
        print(ans[j][i], end="")
