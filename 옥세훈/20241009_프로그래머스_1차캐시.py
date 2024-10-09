from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    cities = [i.lower() for i in cities]

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(i)

    return answer