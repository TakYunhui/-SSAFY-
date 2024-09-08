import pprint

def solution(n, wires):
    answer = -1
    tmp = [[0] * (n + 1) for i in range(n + 1)]
    for wire in wires:
        tmp[wire[0]][wire[1]] = 1
    pprint.pprint(tmp)
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

solution(n, wires)