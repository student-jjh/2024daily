# 일단 아이디어는 다익스트라로 모든 거리 계산때리고 m 이하의 아이템
# 다 더하고 그중 max 출력!
import heapq
import sys
INF = sys.maxsize

N,M,R = map(int,input().split())

items = list(map(int,input().split()))

graph = [[] for _ in range(N+1)]

for _ in range(R):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijstra(i):
    dp[i] = 0

    q = []

    heapq.heappush(q,(0,i))

    while q:
        dist,now = heapq.heappop(q)
        if dp[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[0]

            if cost < dp[node[1]]:
                dp[node[1]] = cost
                heapq.heappush(q,(cost,node[1]))
    cost_graph.append(dp)


cost_graph = []
for i in range(1,N+1):
    dp = [INF for _ in range(N+1)]
    dijstra(i)
answer = 0
for i in range(N):
    temp = 0
    for j in range(N+1):
        if cost_graph[i][j] <= M:
            temp += items[j-1]

    answer = max(answer,temp)
print(answer)