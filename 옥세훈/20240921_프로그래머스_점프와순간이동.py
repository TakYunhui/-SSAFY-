def solution(n):
    ans = 0

    # 한 번에 K 칸(점프) => K만큼의 건전지 소모
    # 현재까지 온거리 * 2(순간이동) => 건전지 소모 없음
    # 건전지 사용량의 최솟값을 구하시오
    # 거리 N
    # 수를 딱 맞춰야하하고 순간이동으로 이동한 후 순간이동하면 현재까지 온거리에 포함

    cost = 1
    while n != 1:

        if n % 2 == 0:
            n = n / 2
        else:
            cost += 1
            n -= 1

    ans = cost
    return ans