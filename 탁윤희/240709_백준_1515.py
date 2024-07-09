# 실버 3 : 수 이어 쓰기
# 숫자 1부터 증가해가며 겹치는 부분이 있는지 확인
# 숫자가 2자리 수 이상이면 모든 자릿 수 중 같은 부분이 있는지 확인
# 만약 같은 부분이 있다면 쓰여진 다음 숫자로 넘어간다
import sys
nums = sys.stdin.readline().rstrip()
n = 0
idx = 0
while True:
    n += 1
    for s in str(n):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()