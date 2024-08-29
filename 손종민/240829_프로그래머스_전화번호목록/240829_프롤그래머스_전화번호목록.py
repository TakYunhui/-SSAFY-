def solution(phone_book):
    answer = True
    dict = {}
    for i in range(len(phone_book)):
        dict[i] = phone_book[i]

    for i in range(len(phone_book) - 1):
        for j in range(i+1, len(phone_book)):
            if dict[i] != phone_book[j] and len(dict[i]) <= len(phone_book[j]):
                count = 0
                for k in range(len(dict[i])):
                    if dict[i][k] != phone_book[j][k]:
                        break
                    else:
                        count += 1
                if count == len(dict[i]):
                    answer = False
                    break
        if answer == False:
            break

    return answer


phone_book = ["123","456","789"]

print(solution(phone_book))