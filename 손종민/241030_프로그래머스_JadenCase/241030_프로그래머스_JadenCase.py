
def solution(s):
    s = list(s)
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ' or s[i] in num:
            answer += s[i]
        else:
            if i == 0 or s[i - 1] == ' ':
                answer += s[i].upper()
            else:
                answer += s[i].lower()


    return answer

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
s = "3people unFollowed me"

print(solution(s))