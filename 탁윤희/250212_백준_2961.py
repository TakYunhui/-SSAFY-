# 실버2. 도영이가 만든 맛있는 음식
# 신맛: 음식의 곱, 쓴맛: 음식의 합
n = int(input())
flavors = []

def sol(start, s, b): # 시작 인덱스, 신맛, 쓴 맛
    global result # result 전역 변수 선언

    if b != 0:
        result = min(result, abs(s-b)) # 신맛 - 쓴맛 절대값

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            # 백트래킹 - 넣었던 거 되돌림
            sol(start+1, s * flavors[i][0], b + flavors[i][1])
            visited[i] = False


for _ in range(n):
    sour, bitter = map(int, input().split())
    flavors.append((sour, bitter))

result = int(1e9) #  모든 재료를 사용해서 요리를 만들었을 때, 그 요리의 신맛과 쓴맛은 모두 1,000,000,000보다 작은 양의 정수이다.
visited = [False] * n # 재료 입력도 0-based로 시작해서 n까지만 구함
sol(0, 1, 0) # 신맛: 곱하기니까 1, 쓴맛: 더하기니까 0

print(result)