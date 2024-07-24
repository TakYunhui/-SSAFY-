# 실버 3. 로마 숫자 만들기
# I, V, X, L
n = int(input())
roma = [1, 5, 10, 50]
arr = [0] * 1001
num = 0
def back(cnt, start):
    global num

    if cnt == n:
        arr[num] = 1
        return

    for i in range(start, 4):
        num += roma[i]
        # 하나 더 해주기
        back(cnt+1, i)
        num -= roma[i]

back(0,0)
print(sum(arr)) # 나온 숫자 개수 세기