import sys
input = sys.stdin.readline

def check_words(word, idx):
    lss = []
    for i in range(len(word)-idx-1):
        check = word[i] + word[i + idx + 1]
        if check in lss:
            return False
        lss.append(check)

    return True

while True:
    words = input().rstrip()
    if words == "*":
        break

    dic = dict()
    words_len = len(words)
    if words_len < 3:
        print(words+" is surprising.")
        continue

    # 총 체크
    flag = False
    for i in range(words_len-2):
        if not check_words(words, i):
            print(words + " is NOT surprising.")
            flag = False
            break
        else:
            flag = True

    last = words[0] + words[-1]
    if flag:
        if last not in dic:
            print(words + " is surprising.")
        else:
            print(words + " is NOT surprising.")