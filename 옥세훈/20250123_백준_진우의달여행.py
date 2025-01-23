n, m = map(int, input().split())

arr =[]
for i in range(n):
  arr.append(list(map(int, input().split())))

# 왼쪽 아래, 아래, 오른쪽 아래
dj = [-1, 0, 1]

# 1행의 열의 수 만큼 반복, 아래로 내려감
# 같은 방향으로 두번연속 못감 -> 구현해야함
# 3개의 방향을 DP적으로 구현 해야함
# 시작점 4곳 순회 시작.

for j in range(n):
  pass
  
     