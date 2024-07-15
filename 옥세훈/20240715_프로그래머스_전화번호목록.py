def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)
    for i in range(1, len(phone_book)):
        if phone_book[0] in phone_book[i]:
            answer = False
            break
    print(answer)
    return answer

solution(["123","12","1235","567","88"])