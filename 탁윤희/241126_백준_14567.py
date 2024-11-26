# 선수과목 이수해야 과목을 들을 수 있음
import sys
input = sys.stdin.readline
# 과목 수, 선수 조건 수
n, m = map(int, input().split())
# m개 줄에 걸쳐 정수 a,b 형태로 선수 과목 주어짐 : a가 b의 선수과목 (a<b)
# -> 단방향성 관계를 가질 듯
subjects = [[] for _ in range(n+1)] # 과목 관계를 인접리스트 형태로 표시할 것
semester = [0] * (n + 1)  # 각 과목의 최소 학기를 저장 (visited 역할도 함)
for _ in range(m):
    a, b = map(int, input().split())
    subjects[b].append(a)

# 1번부터 n번 과목까지 이수에 걸리는 최소 학기를 공백으로 구분해 출력
# 선수과목이 하나라면 그 선수과목 이수 학기 + 1
# 선수과목이 여러 개라면 선수과목들의 이수 학기가 다 같으면 그것 + 1 이고 다르다면 가장 긴 것 + 1
# 선수과목이 없다면 1학기
# 선수과목 여부에 따라 과목 별 이수학기를 다 기록해둬야 할 듯

# DFS 함수
def dfs(subject):
    if semester[subject]:  # 이미 계산된 경우 반환
        return semester[subject]

    if not subjects[subject]:  # 선수 과목이 없는 경우
        semester[subject] = 1
        return 1

    # 선수 과목들의 학기를 계산하여 가장 긴 학기를 선택
    max_sem = 0
    for prerequisite in subjects[subject]:
        max_sem = max(max_sem, dfs(prerequisite))

    semester[subject] = max_sem + 1  # 가장 긴 선수 학기 + 1
    return semester[subject]


# 모든 과목에 대해 최소 학기 계산
for i in range(1, n + 1):
    if semester[i] == 0:  # 아직 계산되지 않은 경우
        dfs(i)

# 결과 출력
print(" ".join(map(str, semester[1:])))