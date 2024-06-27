import itertools

def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0

    num_ls = []
    int_num_ls = set()
    numbers_len = len(numbers)
    for i in range(numbers_len):
        num_ls.append(numbers[i])

    for i in range(1, numbers_len+1):
        check_ls = itertools.permutations(num_ls, i)
        int_num_ls.add(check_ls)

    result_ls = []
    for i in int_num_ls:
        for j in i:
            num = int(''.join(j))
            if num in result_ls or num == 0 or num == 1:
                pass
            else:
                result_ls.append(num)

    print(result_ls)
    for i in result_ls:
        if is_prime_number(i):
            answer += 1

    print(answer)

    return answer

solution("011")
