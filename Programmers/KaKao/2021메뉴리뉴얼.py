from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = []
        max_v = 0
        for order in orders:
            for combi in combinations(sorted(order),c):
                menu.append(''.join(combi))
        combi_menu = Counter(menu)
        for k,v in combi_menu.items():
            if v>=2 and v == max(combi_menu.values()):
                answer.append(k)
                
    answer.sort()

    return answer