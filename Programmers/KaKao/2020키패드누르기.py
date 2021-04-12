def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i == 1 or i == 4 or i== 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i 
        else :
            if i == 0:
                i = 11
            left_calc = abs(i-left)//3 + abs(i-left)%3
            right_calc = abs(i-right)//3 + abs(i-right)%3
            if  left_calc < right_calc:
                answer += 'L'
                left = i
            elif left_calc > right_calc:
                answer += 'R'
                right = i
            else :
                if hand =="right":
                    answer += 'R'
                    right = i 
                else :
                    answer += 'L'
                    left = i
    return answer

