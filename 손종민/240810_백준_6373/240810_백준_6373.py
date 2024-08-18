import sys

sys.stdin = open('input.txt')

input = sys.stdin.read
data = input().split()
is_cyclic = True

for i in range(len(data)):
    this_data = data[i]
    numbers = list(this_data)
    numbers = set(numbers)
    for n in range(1, len(numbers) + 1):
        tmp = int(this_data) * n
        tmp_list = list(str(tmp))
        tmp_list = set(tmp_list)
        if len(tmp_list) == len(numbers):
            if tmp_list != numbers:
                is_cyclic = False
                break
        elif len(tmp_list) + 1 == len(numbers):
            tmp_list.add('0')
            if tmp_list != numbers:
                is_cyclic = False
                break
    
    if is_cyclic == True:
        print(this_data + ' is cyclic')
    else:
        print(this_data + ' is not cyclic')
        is_cyclic = True