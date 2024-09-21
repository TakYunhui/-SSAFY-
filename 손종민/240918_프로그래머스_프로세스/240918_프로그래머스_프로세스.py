from collections import deque

def solution(priorities, location):
    answer = 1
    processes = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)
    while priorities :
        isActivated = True
        this_process = processes.popleft()
        this_process_priorities = priorities.popleft()
        for priority in priorities:
            if priority > this_process_priorities:
                priorities.append(this_process_priorities)
                processes.append(this_process)
                isActivated = False
                break        
        if isActivated == True:
            if this_process == location:
                break
            else:
                answer += 1
    
    return answer

priorities = [1, 1, 9, 1, 1, 1]

location = 0

print(solution(priorities, location))