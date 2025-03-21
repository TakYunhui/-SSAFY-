# 실버2. 박스 나누기 게임
# 상대에게 (홀수, 홀수)를 넘겨주면 이긴다
n, m = map(int, input().split())
# n, m이 둘다 홀수면 b 승리 아니면 a
print("B") if n * m % 2 == 1 else print("A")