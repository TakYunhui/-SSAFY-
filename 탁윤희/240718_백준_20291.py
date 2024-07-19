# 실버 3. 파일 정리
# 확장자별 + 사전순으로 정렬
# 총 50,000개의 N => dict로 정리한다면?
import sys
input = sys.stdin.readline
n = int(input())
result = dict()
# 확장자 "." 기준으로 분리해 dict에 넣기
for i in range(n):
    file = input().rstrip().split(".")
    result[file[1]] = result.get(file[1], 0) + 1
# 사전 순으로 정렬 후 출력
result = sorted(result.items())
for i in result:
    print(i[0], i[1])