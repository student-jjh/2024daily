def ara(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes
N = int(input())
temp=ara(N+1)
temp.append(0)

cnt = 0
i,j = 0,0
sm = temp[0]
while j != len(temp)-1:
    if sm == N :
        cnt +=1
        j+=1
        sm += temp[j]
    elif sm < N:
        j += 1
        sm += temp[j]

    else:
        sm -= temp[i]
        i += 1

print(cnt)