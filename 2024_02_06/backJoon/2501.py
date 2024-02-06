N,K = map(int,input().split())

temp = []

for i in range(1,N+1):
    if N % i == 0:
        temp.append(i)

if len(temp) < K:
    print(0)
else:
    print(temp[K-1])