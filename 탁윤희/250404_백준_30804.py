# 실버 2. 과일 탕후루
n = int(input())
fruit = list(map(int, input().split()))
# 앞쪽, 뒤쪽 몇 개 빼서 두 종류 이하 과일만 남기기 => 정렬 x
# 과일 개수 가장 많은 것
l = 0
fruit_cnt = {}
max_len = 0

for r in range(n):
    current_fruit = fruit[r]
    # 현재 과일이 과일 종류에 없으면 1 선언, 있으면 1추가
    if current_fruit in fruit_cnt:
        fruit_cnt[current_fruit] += 1
    else:
        fruit_cnt[current_fruit] = 1
    # 과일 종류가 2개 이상이면
    while len(fruit_cnt) > 2:
        # 제일 왼쪽 과일 제거, 과일 종류 딕셔너리에서 1 삭제
        fruit_to_remove = fruit[l]
        fruit_cnt[fruit_to_remove] -= 1
        # 만약 삭제된 과일 종류 개수가 0이면 아예 딕셔너리에서 제거
        if fruit_cnt[fruit_to_remove] == 0:
            del fruit_cnt[fruit_to_remove]
        l += 1 # 왼쪽 인덱스 이동

    max_len = max(max_len, r - l + 1)

print(max_len)




