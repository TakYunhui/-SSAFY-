# 실버 5 : 사과담기 게임
# 스크린 n칸, 바구니 m칸, 떨어지는 사과 개수 j
# 바구니는 가장 처음 무조건 왼쪽부터 m칸! (0번째부터 시작)
# 사과 칸의 번호가 m의 이동 범위 안에 있으면 그만큼 움직인 걸 더한다
# x, y로 바구니의 범위를 지정하고 delta 이동시키듯 이동시켜보기
# 이때 사과 번호가 끝 범위보다 크면 -1 로 이동시켜야 됨

n, m = map(int, input().split())
j = int(input())
result = 0
x = 1

for i in range(j): # 사과 개수만큼 반복
    apple = int(input())
    while True:
        if apple in range(x, x+m):
            break
        else:
            result += 1
            if apple > x:
                x += 1
            elif apple < x:
                x -= 1

print(result)
