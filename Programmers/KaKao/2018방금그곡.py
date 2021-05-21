def solution(m, musicinfos):
    answer = ''
    change = {'C#':'c', 'D#':'d', 'E#':'e','F#':'f', 'G#':"g", 'A#':"a"}
    musics = {}
    for musicinfo in musicinfos:
        start,end,title,music = musicinfo.split(',')
        start,end = list(map(int,start.split(':'))), list(map(int,end.split(':')))
        time = (end[0]-start[0])*60 + end[1]-start[1]
        
        for k,v in change.items():
            music = music.replace(k,v)
            m  = m.replace(k,v)
            
        if time <= len(music):
            musics[music[:time]] = title
        else:
            r,d = time//len(music) , time%len(music)
            musics[music*r + music[:d]] = title

    max_music = 0
    for k,v in musics.items():
        if m in k:
            if len(k)>max_music:
                answer = v
                max_music = len(k)
    if answer == '':
        answer  = "(None)"      
    return answer
