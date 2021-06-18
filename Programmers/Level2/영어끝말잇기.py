def solution(n, words):
    answer = []
    people = []
    next_word = ''
    for idx,word in enumerate(words):
        if people and (word in people or next_word != word[0]):
            answer.append((idx%n)+1)
            answer.append((idx//n)+1)
            break
        else:
            people.append(word)
            
        next_word = word[-1]

    if not answer:
        answer = [0,0]
        

    return answer

