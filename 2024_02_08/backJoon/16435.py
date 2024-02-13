N,L = map(int,input().split())

fr = list(map(int,input().split()))
fr.sort()

for i in range(N):
    if fr[i] <= L:
        L +=1
    else:
        break

print(L)