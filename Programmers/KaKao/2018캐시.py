def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5
    
    for city in cities:
        if city.lower() not in cache:
            answer += 5
            if len(cache) < cacheSize :
                cache.append(city.lower())
            else :
                cache.pop(0)
                cache.append(city.lower())
        else :
            answer += 1
            cache.pop(cache.index(city.lower()))
            cache.append(city.lower())
            
    return answer

