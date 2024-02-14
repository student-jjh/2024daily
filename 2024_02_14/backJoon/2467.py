N = int(input())
i,j = 0,N-1

lst = list(map(int,input().split()))
ai,aj = lst[0],lst[N-1]
sm = lst[i] + lst[j]
answer = lst[i] + lst[j]
while j > i:
    if sm > 0:
        sm-=lst[j]
        j-=1
        sm+=lst[j]
    else:
        sm-=lst[i]
        i+=1
        sm+=lst[i]
    if abs(sm) < abs(answer) and i!=j:
        answer = sm
        ai,aj = lst[i],lst[j]

print(ai,aj)
