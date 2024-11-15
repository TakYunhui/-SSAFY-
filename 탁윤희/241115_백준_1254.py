# 실버2. 팰린드롬 만들기
# 내 생각: 슬라이스로 대응되는 부분들 일치여부확인하기?
# 홀수라면 가운데 인덱스 제외하고 보다가 안 일치하면 뭔가 생각해야 함
# s = input()
# n = len(s)
# not_equal = 0
# print(n)
# for i in range(n//2):
#     print(i, -(i+1))
#     print(s[i], s[-(i+1)])
#     print(s[i] == s[-(i+1)])
#     # 만약 얘들이 같으면 넘어가는데, 문제는 같다가 안 같아지는 부분이 있음 걔때문에 결국 더 넣어야 할 듯?


# 풀이참고 : https://fre2-dom.tistory.com/322
# 완전 이상한 생각을 한 듯..
s = input()
for i in range(len(s)): # 반복문 문자 확인
    # i번째로 시작한 문자열과 i번째로 시작한 문자를 뒤에서부터 확인한 문자열 비교
    # ==> 뭔말이냐면 슬라이스 하나씩 줄여가면서 앞에서 시작 문자열 | 뒤에서 시작 문자열 같은지 확인

    # print(s[i:], s[i:][::-1], i)
    # abdfhdyrbdbsdfghjkllkjhgfds
    # abdfhdyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbrydhfdba
    # 0
    # bdfhdyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbrydhfdb
    # 1
    # dfhdyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbrydhfd
    # 2
    # fhdyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbrydhf
    # 3
    # hdyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbrydh
    # 4
    # dyrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbryd
    # 5
    # yrbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbry
    # 6
    # rbdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdbr
    # 7
    # bdbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbdb
    # 8
    # dbsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsbd
    # 9
    # bsdfghjkllkjhgfds
    # sdfghjkllkjhgfdsb
    # 10
    # sdfghjkllkjhgfds
    # sdfghjkllkjhgfds
    # 11
    # 11
    # 38
    if s[i:] == s[i:][::-1]:
        # 문자열이 같을 때, 기존 문자에 i개 문자를 추가해주면 팰린드롬이 됨
        print(len(s) + i)
        break