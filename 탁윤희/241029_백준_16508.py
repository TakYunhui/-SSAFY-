# # 실버3. 전공책
# t = input() # 만들고자 하는 단어 문자열
# n = int(input()) # 가진 전공책의 개수(정수)
# # 가격, 이름 한 줄로 입력받는 허세 - name에 join처리 안 해주면 리스트로 나옴 ㄷㄷ
# # ㄴ *가 리스트 언패킹 형태로 input().split()으로 나눈 나머지를 전부 리스트로 담기 때문임!
# books = list((int(p), ''.join(name)) for p, *name in (input().split() for _ in range(n)))
#
# # 가장 적은 비용으로 t를 만들 것
# # => 각 책이 가지는 t의 일부 개수를 판단하여 저장해둔다
# # 부족하면 뒤의 책에서 가져오는 형태인데 애초에 가격 순으로 책을 정렬하고 단어를 만족하는지도 판단하면 더 빨리 끝날 듯!!
# books.sort(key=lambda x:x[0])
#
# # 단어 만드는데 필요한 알파벳 갯수들 구함
# required_letters = {}
# for letter in t:
#     required_letters[letter] = required_letters.get(letter, 0) + 1
#
# result = 0 # 출력할 책 가격 total 값
# remaining_letters = required_letters.copy() # 필요한 알파벳 카운트 저장
# for price, title in books:
#     available_letters = {}
#     # 1차 아이디어
#     # 여기서 title안에 word 글자들을 얼마나 구현할 수 있는지 확인
#     # 일부만 확인되면 그만큼만 tmp 변수에 저장해둔다
#     # 뒤에 더 싸게 한번에 처리되면 tmp 갱신, 가격 갱신

# 답지 참고 - 근데 좀 더 이해해야 함
from collections import Counter
import sys

def min_cost_to_form_word(target_word, books):
    # 목표 단어의 각 글자 개수
    target_count = Counter(target_word)
    n = len(books)
    min_cost = sys.maxsize

    # 각 책의 제목에 포함된 글자 개수 계산
    book_letters = [Counter(title) for _, title in books]

    # 모든 책의 부분집합을 탐색
    for subset in range(1, 1 << n):  # 1 << n 은 2^n, 모든 부분집합을 순회
        current_count = Counter()
        total_cost = 0

        # 선택된 책들의 부분집합에서 글자 개수 누적
        for i in range(n):
            if subset & (1 << i):  # i번째 책이 선택된 경우
                price, title = books[i]
                current_count += book_letters[i]
                total_cost += price

        # 현재 부분집합이 목표 단어를 만들 수 있는지 확인
        can_form_word = all(current_count[char] >= target_count[char] for char in target_count)
        if can_form_word:
            min_cost = min(min_cost, total_cost)

    # 결과 출력
    return min_cost if min_cost != sys.maxsize else -1

# 입력 처리 예시
target_word = input().strip()
n = int(input().strip())
books = []
for _ in range(n):
    price, title = input().split()
    books.append((int(price), title))

# 결과 출력
print(min_cost_to_form_word(target_word, books))
