def solution(s):
    answer = 0
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i,word in enumerate(words):
        s = s.replace(word,str(i))
        
    answer = int(s)
    return answer