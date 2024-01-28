N, K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

k = 0

while k < K:
    if A[k] > B[k]:
        break

    else:
        A[k],B[k] = B[k],A[k]
    
    k +=1

print(sum(A))