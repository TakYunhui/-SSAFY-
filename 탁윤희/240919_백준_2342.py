# 실버 1. 기타 레슨
# m개 똑같은 길이 만들기
n, m = map(int, input().split())
lessons = list(map(int, input().split()))
# 블루레이 최소: 가장 긴 강의, 최대: 전체 강의 합
left, right = max(lessons), sum(lessons)
while left <= right:
    mid = (left + right) // 2
    cnt = 1 # 사용한 블루레이 개수 (* 최소 하나는 사용)
    current_sum = 0 # 현재 블루레이에 담긴 강의의 길이 합

    # 강의를 확인하며 블루레이에 담기
    for lesson in lessons:
        # 안 담아지면 새 블루레이 사용
        if current_sum + lesson > mid:
            cnt += 1
            current_sum = lesson # 현재 강의를 새 블루레이에 담음
        else:
            current_sum += lesson
    # 블루레이 사용 개수가 m개 이하면 크기를 줄일 수 있따
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)

