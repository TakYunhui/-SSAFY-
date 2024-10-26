# 플그2. 프로세스 (스택/큐)
# 스택 pop(0)으로도 풀 수 있지만 이는 성능 상 O(n)의 시간복잡도를 가짐
# ㄴ 리스트의 다른 요소들을 앞으로 한 칸씩 이동시키게 되기 때문
# 반면 큐는 양쪽에서 삽입/삭제가 가능한 이중 연결 리스트 - 첫 번째 요소를 제거할 때 이동 없이 바로 제거되어 O(1)
from collections import deque

def solution(priorities, location):
    answer = 0
    # idx로 location이 맞는지 판별해야하니 배열에 우선순위 중요도와 idx 같이 저장한다! 
    # enumerate: 반복 가능한(iterable) 객체에서 요소와 우선순위를 함께 가져올 수 있다
    # 첫번째 i: 인덱스, 두번째: 요소
    queue = deque((p, i) for i, p in enumerate(priorities))

    # For문으로 index 별로 한번만 조회해서는 숫자를 넣고 뺐다를 할 수 없다 -> while문?
    while queue:
        # 현재 프로세스를 큐에서 꺼냄 (우선순위, 인덱스)
        current = queue.popleft()
        # any: 주어진 조건이 하나라도 참이면 True 반환
        # any(조건 for 요소 in iterable)
        # 현재 우선순위보다 높은 우선순위가 있는지 확인
        if any(current[0] < q[0] for q in queue):
            # 우선순위가 높은 프로세스가 있으면 다시 큐에 넣음
            queue.append(current)
        else:
            # 실행된 순서 증가 - 위 if문에서 증가하면 실제로 실행되지 않고 넘어간 것도 다 증가됨!!
            answer += 1
            # 목표 위치면 answer 반환
            if current[1] == location:
                return answer

    return answer