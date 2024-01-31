N = int(input())

temp = list(map(int,input().split()))

dp1 = [0 for _ in range(N)]
dp2 = [0 for _ in range(N)]

dp1[0] =1
dp2[0] =1
for i in range(1,N):
    if temp[i] >= temp[i-1]:
        dp1[i] = dp1[i-1] +1
    else:
        dp1[i] = 1
    if temp[i] <= temp[i-1]:
        dp2[i] = dp2[i-1] +1
    else:
        dp2[i] = 1

print(max(max(dp1),max(dp2)))
