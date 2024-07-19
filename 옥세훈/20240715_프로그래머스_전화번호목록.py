def solution(phone_book):

    for _ in phone_book:
        check = phone_book.pop(0)
        for i in range(1, len(check)):
            checkk = check[:i]
            if checkk in phone_book:
                return False

    return True

solution(["123","12","1235","567","88"])