def solution(genres, plays):
    answer = []
    genre_total = dict()
    genre_plays = dict()
    
    for i,genre in enumerate(genres):
        if genre not in genre_plays:
            genre_plays[genre] = []
        if genre not in genre_total:
            genre_total[genre] = 0
        genre_plays[genre].append([plays[i],i])
        genre_total[genre] += plays[i]

    genre_total = sorted(genre_total.items(), key=lambda item:item[1],reverse=True)
    
    for key,value in genre_total:
        genre_plays[key] = sorted(genre_plays[key], key=lambda x:(x[0],-x[1]))
        cnt = 0 
        while genre_plays[key] and cnt != 2 : 
            temp = genre_plays[key].pop()
            answer.append(temp[1])
            cnt += 1
   
    return answer

    

