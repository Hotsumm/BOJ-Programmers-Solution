def solution(record):
    answer = []
    user_list = dict()

    for i in record:
        if i.split(' ')[0] != 'Leave':
            user_list[i.split(' ')[1]] = i.split(' ')[2]
            
    for i in record:
        if i.split(' ')[0] == "Enter":
            answer.append(user_list[i.split(' ')[1]]+"님이 들어왔습니다.")
        elif i.split(' ')[0] == "Leave":
             answer.append(user_list[i.split(' ')[1]]+"님이 나갔습니다.")
    
    return answer