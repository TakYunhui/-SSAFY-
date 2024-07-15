# 실버 3. 가희와 키워드
# 아이디어 - 집합에서 공통된 거 없애기? => 시간 초과
# 아이디어(풀이 참고) - dictionary 사용
# ㄴ 이것도 sys 안 쓰면 시간초과남
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 키워드 개수, 블로그 글 개수
keywords = dict()
remains = 0

for i in range(n):
    keywords[input().rstrip()] = 1
    remains += 1

for i in range(m):
    words = input().rstrip().split(",")
    for j in words:
        if keywords.get(j):
            remains -= 1
            del keywords[j]
    print(remains)


