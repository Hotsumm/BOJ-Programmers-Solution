import sys

s,e,q = list(sys.stdin.readline().rstrip().split())
s,e,q = int(s.replace(':','')),int(e.replace(':','')),int(q.replace(':',''))

attendance = dict()
cnt = 0
while True:
    line = sys.stdin.readline()
    if len(line) < 5:
        break
    time, nickname = map(str,line.split())
    time = int(time.replace(':',''))
    if time<=s:
        attendance[nickname] = 1
    elif e<=time<=q and attendance.get(nickname) == 1 :
        cnt += 1
        attendance[nickname] += 1
print(cnt)
