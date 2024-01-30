import sys
INF = sys.maxsize

sq_list = [x**2 for x in range(1,318)]

N = int(input())

dp = [INF] * (N+1)

i = 0
while sq_list[i] <= N:
    temp = sq_list[i]
    dp[temp] = 1

    for j in range(temp +1,N+1):
        if dp[j] > dp[j-temp] +1:
            dp[j] = dp[j-temp] +1

    i +=1

print(dp[N])