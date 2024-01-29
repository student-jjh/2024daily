N = int(input())

graph = []
dp = [0 for _ in range(N+1)]
for _ in range(N):
    graph.append(int(input()))

if N == 1:
    print(graph[0])

elif N ==2:
    print(sum(graph[:2]))


else:
    dp[0] = graph[0]
    dp[1] = graph[0] + graph[1]
    dp[2] = max(graph[2] + graph[0],graph[1] +graph[2])

    for i in range(3,N):
        dp[i] = max(dp[i-2]+ graph[i],dp[i-3] + graph[i] + graph[i-1])

    print(dp[N-1])
