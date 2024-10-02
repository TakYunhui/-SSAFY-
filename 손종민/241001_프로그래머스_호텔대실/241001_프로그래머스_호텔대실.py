from collections import deque

def solution(book_time):
    answer = 0
    book_time.sort()
    book_time = deque(book_time)
    using_room = deque()
    while book_time:
        # 사용중인 방이 없으면
        if not using_room:
            # 사용중으로 바꿔주기
            using_room.append(book_time.popleft())
            answer += 1
        
        # 사용중인 방이 있으면
        else:
            this_room = book_time.popleft()
            is_empty = False
            for i in range(len(using_room)):
                difference_time = minus_time(this_room[0], using_room[i][1])
                if difference_time >= 10:
                    is_empty = True
                    using_room.remove(using_room[i])
                    using_room.append(this_room)
                    break
            # print(using_room)
                    
            if is_empty != True:
                using_room.append(this_room)
                answer += 1
            else:
                is_empty = False



    return answer

def minus_time(time_a, time_b):
    answer = 0
    a = time_a.split(':')
    b = time_b.split(':')
    minus_hour = int(a[0]) - int(b[0])
    minus_minute = int(a[1]) - int(b[1])
    answer += minus_hour * 60
    if minus_minute >= 0:
        answer += minus_minute
    else:
        answer -= (60 - minus_minute)

    return answer


book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]

print(solution(book_time))