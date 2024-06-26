# 실버 5 : 줄 세우기
# 총 학생 20명, 같은 키 x
# 아무나 줄의 맨 앞에 세우고 그 뒤에 한명 씩
# 자기 앞에 자기보다 키 큰 학생이 없다면 그자리
# 키큰 학생이 한 명 이상 있다면 가장 앞에 있는 학생 a 바로 앞
# a부터 뒤의 모든 학생은 뒤로 밀림
# => 버블 정렬
def bubblesort(list):
    global result
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                result += 1

p = int(input()) # 테스트 케이스 수
for i in range(p):
    t, *students = map(int, input().split()) # 테스트 번호와 학생들 키
    result = 0
    bubblesort(students)

    print(f'{t} {result}') # 번호와 결과 출력