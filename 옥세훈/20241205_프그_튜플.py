def solution(s):
    answer = []

    s = s[1:-1]
    numbers = []
    # print(s)

    for i in range(len(s)):
        if s[i] == "{":
            check = []
        elif s[i] == "}":
            answer.append(check)
        elif s[i].isdigit():
            numbers.append(s[i])
            # if s[i] == "0":
            #     print(s[i])
            #     print(numbers)
        elif s[i] == ",":
            num = ""
            while numbers:
                num += numbers.pop(0)
                # print(num)
            check.append(int(num))
        elif numbers:
            num = ""
            while numbers:
                num += numbers.pop()
            check.append(int(num))

    num = ""        
    while numbers:
        num += numbers.pop(0)

    answer[-1].append(int(num))

    arr = sorted(answer, key=lambda x : len(x))

    last = []
    for i in arr:
        for j in i:
            if j not in last:
                last.append(j)

    return last