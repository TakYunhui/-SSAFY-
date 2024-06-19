# 20920 영단어 암기는 괴로워
# 풀이 전략
# 각 String 길이 재고
# 우선 순위 : 자주 나오는 단어, 해당 단어의 길이가 길수록, 알파벳순
# 자주 나오는 단어, 단어 길이는 카운트 필요 
# 단어별로 빈도 수를 어떻게 체크하지?
# 클래스로 접근해보려 했으나... 쉽지 않네
# 우선 순위 반대 순서로 정렬해야 할 듯?

# import sys
# sys.stdin = open('input.txt')

# N, M = map(int, input().split(' '))
# temp = []
# count = []

# for _ in range(N):
#     word = input()

#     if len(word) >= M:
#         temp.append(word)

#     temp.sort() # abc 순 정렬 완료


        
    

# for tempword in temp:
#     print(tempword)


# 풀이 
# 딕셔너리 구조와 lambda 함수를 활용해야 함

from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict_dict = defaultdict(int) # 딕셔너리 선언

for _ in range(N) :
    word = input().strip()
    if len(word) >= M:              # M보다 크면
        dict_dict[word] += 1        # word key에 value 1 추가해주기

dict_list = list(dict_dict.keys())  # 딕셔너리의 key 밸류인 word 리스트 추가
dict_list.sort(key = lambda x : (-dict_dict[x], -len(x), x)) # 우선순위 따라 정렬 : 각 x는 1) dict_dict[x] 의 숫자 크기 내림차순,  x의 길이 내림차순, x의 순서 오름차순 순서로 나열
for word in dict_list :
    print(word)


# 왜 못 풀었을까?
# 딕셔너리 구조 자체를 오랜만에 보는데... 클래스 형태든 뭐든 따로 기록해야겠다고 접근은 했다.
# 딕셔너리 활용법 기억하기
# strip() 활용법 기억하기
# lambda 함수 미숙함 => 여러 조건 정렬할 때에는 사용하는 게 좋을 것 같다.