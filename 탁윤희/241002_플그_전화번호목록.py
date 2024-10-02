def solution(phone_book):
    # 정렬 시, 접두어를 사용한 번호는 가까이 있게 됨
    phone_book.sort()
    # 전화번호 순회 : 현재 번호와 다음 번호 비교
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False # 하나라도 나오면 바로 False 반환하며 종료
    return True