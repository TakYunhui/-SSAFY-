def solution(s):
    answer = []
    cnt_check = 0
    cnt_zero = 0
    new_2 = ""

    while True:
        if new_2 == "1":
            break

        cnt_zero += s.count("0")
        new_2 = s.replace("0", '')

        new_2 = bin(len(new_2))[2:]
        print(new_2)
        cnt_check += 1
        s = new_2

    return answer

solution("110010101001")