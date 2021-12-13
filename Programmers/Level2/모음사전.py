from itertools import product

def solution(word):
    answer = 0
    str_list = []
    
    for i in range(1,6):
        for p in product(['A','E','I','O','U'],repeat=i):
            _str = ''.join(p)
            str_list.append(_str)
    str_list.sort()

    answer = str_list.index(word) + 1
    
    return answer
