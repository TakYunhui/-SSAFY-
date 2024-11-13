from collections import deque

def solution(cacheSize, cities):
    que = deque([])
    answer = 0
    for city in cities:
        # 큐에 해당 건이 없고 캐시가 꽉차지 않았을 때
        city = city.lower()
        if city not in que and len(que) < cacheSize:
            que.append(city)
            answer += 5
        elif city not in que and len(que) >= cacheSize:
            if cacheSize != 0:
                que.popleft()
                que.append(city)
            answer += 5
        elif city in que:
            que.remove(city)
            que.append(city)
            answer += 1
        
    return answer

cacheSize = 2

cities = ["a", "b", "a", "a", "b"]

print(solution(cacheSize, cities))