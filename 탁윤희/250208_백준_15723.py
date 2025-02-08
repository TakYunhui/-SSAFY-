# 실버1. n단논법
# n개의 줄에 걸쳐 숫자가 아닌 문자 입력 -> 숫자 형태의 인덱스 저장은 불가
# => 문자열 인덱스 이용
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(alphabet) # 알파벳 사이즈 크기 변수명 확실히 할 것 - 혼동없게 한다
graph = [[INF] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)] # 이중 리스트 : 전체 알파벳 크기를 이용하여 각 알파벳 별로 모든 알파벳과 대응하는 인덱스를 가지는 리스트 생성

for _ in range(n):
    # " is " 기준으로 입력 문자열을 나눠 a, b 분리해 받음
    # alphabet.index를 통해 alphabet 문자열 변수에서 a, b 변수 값이 가지는 인덱스(번호) 호출
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    # a == b로 단방향 연결
    graph[a][b] = 1

# 플로이드-워셜 알고리즘 : 정점 간 최단 경로 구함
for k in range(ALPHABET_SIZE):# 모든 알파벳 노드를 중간 경유지로 고려
    for i in range(ALPHABET_SIZE):# 출발 노드 i
        for j in range(ALPHABET_SIZE):# 도착 노드 j
            # 기존 경로 비용 graph[i][j]
            # i > k > j 경로 비용 : graph[i][k] + graph[k][j]
            # 위 2개의 비용을 비교 해 더 작은 값으로 갱신
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

m = int(input())
for _ in range(m):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    # 경로 비용이 INF 라면 연결된 노드가 없었단 뜻
    if graph[a][b] == INF:
        print("F")
    else:
        print("T")
