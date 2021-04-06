cnt=1
while True:
    L,P,V = map(int,input().split())
    if L==0 and P==0 and V==0:
        break
    print("Case",str(cnt)+":",str((V//P)*L + (L if V%P>=L else V%P)))
    cnt += 1