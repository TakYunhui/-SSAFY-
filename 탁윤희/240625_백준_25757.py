# 실버 5 : 임스와 함께 하는 미니 게임
# 윷놀이 Y(2), 그림 찾기 F(3), 원카드 O(4)
# 인원수가 부족하면 게임 X
# 게임 신청 사람 수 N, 플레이할 게임 종류 => 최대 게임횟수
# 한 번 게임한 사람은 다시 플레이 X => 같은 사람은 1번만 저장해
# 임스는 무조건 게임에 들어가니까 각 필요 인원수 -1 한 사람만 구하면 됨
# 첫번째 입력 : 게임 신청 횟수 + 게임 종류
# 두번째 입력 : 플레이하고자 하는 사람들의 이름 문자열
n, game = input().split()
n = int(n)

people = set(input() for i in range(n))
people = len(people)

if game == "Y":
    print(people)
elif game == "F":
    print(people // 2)
else:
    print(people // 3)
