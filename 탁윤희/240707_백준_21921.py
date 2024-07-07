# 블로그 - 실버 3
# x일 동안 가장 많이 들어온 방문자 수 출력 => x만큼의 누적합
# 최대 방문자 수가 0이면 SAD
# 최대 방문자 수가 0이 아니면 방문자 수 + 기간
# => 누적합 중 최댓값 + 그 최댓값 빈도 수 출력
n, x = map(int, input().split())
visits = list(map(int, input().split()))
# 누적합 기반 슬라이딩 윈도우 기법 사용
# => 누적합 배열을 만들지 않고 윈도우를 이동시키며 방문자 수 합 업데이트
# 초기값 선언: 배열 처음 x개의 요소의 합
current_sum = sum(visits[:x])
max_sum = current_sum
count = 1
# 슬라이딩 윈도우 기법으로 방문자 수 합 갱신
# 배열에서 연속된 x개의 요소의 합 구하기
for i in range(x, n):
    # 윈도우를 한 칸 오른쪽으로 이동시키면서 이전 윈도우의 첫번째 요소 빼기
    # + 새로운 요소를 더 해 합을 업데이트
    current_sum = current_sum - visits[i - x] + visits[i]
    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

# 결과 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)