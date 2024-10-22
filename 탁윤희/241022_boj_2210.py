# 실버2. 숫자판 점프
# 5 * 5 숫자판 받기
numbers = list(list(input().split()) for _ in range(5))
result = set()
# dfs 함수 만들기 - 6글자를 만들 때까지 재귀
def dfs(x, y, number):
    if len(number) == 6:
        result.add(number)
        return

    d = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    for k in range(4):
        dx = x + d[k][0]
        dy = y + d[k][1]

        if 0 <= dx < 5 and 0 <= dy < 5: # 숫자 판 범위 내라면
            # 좌표 이동 + 문자열에 이동한 좌표의 문자 추가
            dfs(dx, dy, number + numbers[dx][dy])

# 5 * 5 의 모든 자리(좌표)를 대입해서 숫자 만들기
for i in range(5):
    for j in range(5):
        # 좌표 + 첫번째 숫자(== 내가 만들 6자리 문자열)
        dfs(i, j, numbers[i][j])


print(len(result))