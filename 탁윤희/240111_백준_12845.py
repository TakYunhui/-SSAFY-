# 실버3. 모두의 마블
# 업그레이드된 카드 레벨 따라감 -> 가장 높은 레벨 카드를 업그레이드
# 결국 가장 큰 레벨에 계속 다른 카드를 합쳐주게 된다
import sys
input = sys.stdin.readline

n = int(input())
levels = list(map(int, input().split()))
levels.sort(reverse=True)
result = 0
for i in range(n-1):
    i = 0 # 가장 큰 수는 levels[0]이므로 i를 항상 0으로 초기화
    result += levels[i] + levels[i+1]

    # del : 리스트에서 특정 인덱스 요소 삭제
    del levels[i+1] # 업그레이드에 쓴 카드는 제거
print(result)
