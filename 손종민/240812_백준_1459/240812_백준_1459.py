import sys

sys.stdin = open('input.txt')

# 블록을 거쳐 갈 경우
# 대각으로 가로질러 갈 경우
# X, Y 중 하나가 더 길 때
# W * 2랑 S 비교
# W * 2보다 S가 더 걸릴 경우, S는 고려할 필요도 없다.
# 반대의 경우, 

X, Y, W, S = map(int, input().split(' '))

result = 0

# X, Y가 0보다 큰 동안
while X > 0 or Y > 0:
    # 하나가 0이라 직선 구간만 생각할 경우
    if X == 0:
        if W < S:
            result += W
        else:
            result += S
        Y -= 1
    elif Y == 0:
        if W < S:
            result += W
        else:
            result += S
        X -= 1
    else:

        X -= 1
        Y -= 1
        if W * 2 < S:
            result += W * 2
        else:
            result += S


print(result)