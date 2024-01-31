import sys
INF = sys.maxsize

N = int(input())

temp_list = list(map(int,input().split()))
dp = [INF for _ in range(N)]

dp[0] = 0

for i in range(N):
    for j in range(1,temp_list[i]+1):
        if i+j >= N:
            break
        if dp[i+j] > dp[i] + 1:
            dp[i+j] = dp[i] +1
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
