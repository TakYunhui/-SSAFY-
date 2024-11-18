alphabets = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R':18, 'S': 19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26 }

def solution(msg):
    answer = []
    dict_length = 26
    tmp = ''
    for i in range(len(msg)):
        length = i
        tmp = msg[length]
        while tmp:
            if i == len(msg) - 1:
                answer.append(alphabets[tmp])
                break
            if tmp in alphabets and length < len(msg) - 1:
                if alphabets[tmp] in answer:
                    # answer.append(alphabets[tmp])
                    length += 1
                    tmp += msg[length]
                else:
                    answer.append(alphabets[tmp])
                    length += 1
                    tmp += msg[length]
            else:
                dict_length += 1
                alphabets[tmp] = dict_length
                break

    return answer

print(solution('ABABABABABABABAB'))