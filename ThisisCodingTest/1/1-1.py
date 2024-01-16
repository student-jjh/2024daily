N,K = map(int,input().split())

answer = 0

while N != 1:
    if N % K == 0 : 
        answer+=1
        N = N // K

    else:
        answer+=1
        N -= 1
print(answer)

