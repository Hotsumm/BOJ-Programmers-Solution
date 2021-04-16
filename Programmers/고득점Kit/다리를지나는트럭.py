def solution(bridge_length, weight, truck_weights):
    answer = 0
    st = [0] * bridge_length
    while st:
        answer += 1 
        st.pop(0)
        if truck_weights:
            if sum(st) + truck_weights[0] <= weight:
                st.append(truck_weights.pop(0))
            else :
                st.append(0)
    return answer




