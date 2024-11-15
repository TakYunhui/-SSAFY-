def solution(str1, str2):
    str1_tmp = make_input(str1)
    str2_tmp = make_input(str2)
    sum_strs = list(tuple(str1_tmp + str2_tmp))
    union_strs = []
    tmp_str = []
    another_str = []
    tmp_length = 0
    if len(str1_tmp) >= len(str2_tmp):
         tmp_length = len(str2_tmp)
         tmp_str = str2_tmp
         another_str = str1_tmp
    else:
         tmp_length = len(str1_tmp)
         tmp_str = str1_tmp
         another_str = str2_tmp

    for i in range(tmp_length):
         if tmp_str[i] in another_str:
              union_strs.append(tmp_str[i])
              sum_strs.remove(tmp_str[i])
    cluster = int(len(union_strs) / len(sum_strs) * 65536)
    return cluster



def make_input(strings):
        str_tmp = []
        for i in range(len(strings) - 1):
            word = strings[i].lower()
            if word.isalpha() or word.isdigit():
                if strings[i + 1].isalpha() or strings[i + 1].isdigit():
                    str_tmp.append(word + strings[i + 1].lower())
        return str_tmp

str1 = 'aa1+aa2'
str2 = 'AAAA12'

print(solution(str1, str2))