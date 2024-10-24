# 실버3. 삼각형 만들기
import sys
input = sys.stdin.readline

n = int(input())
straws = []
for _ in range(n):
    straw = int(input())
    straws.append(straw)
# 가장 긴 빨대들부터 사용하기 위해 내림차순 정렬
straws.sort(reverse=True)
for i in range(n):
    # i + 2가 n을 넘으면 index error
    if i + 2 < n:
        # 가장 긴 변, 그 다음 변, 그 다음다음 변
        a, b, c = straws[i], straws[i+1], straws[i+2]
        # 삼각형의 불등식 - 가장 긴변이 나머지 두 변의 합보다 작으면 ok
        if a < b + c :
            print(a + b + c)
            break
# 만약 for문 돌며 if문 만족 못 했다면 삼각형 못 만들었으니 -1 출력
else:
    print(-1)