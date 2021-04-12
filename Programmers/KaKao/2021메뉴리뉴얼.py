from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        menu = []
        for order in orders:
            for combi in combinations(order,i):
                menu.append(''.join(sorted(combi)))
        print(menu)
    return answer


