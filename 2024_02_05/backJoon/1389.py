import heapq
import sys
INF = sys.maxsize

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = []
def dijstra(graph,s):
    visited=[INF for _ in range(N+1)]
    q = []
    visited[s] = 0

    heapq.heappush(q,(0,s))

    while q:
        dist,now = heapq.heappop(q)

        if dist > visited[now]:
            continue

        for node in graph[now]:

            cost = dist + 1
            if visited[node] > cost:
                visited[node] = cost
                heapq.heappush(q,(cost,node))
    for i in range(N+1):
        if visited[i] == INF:
            visited[i] = 0

    answer.append(sum(visited))

for i in range(1,N+1):
    dijstra(graph,i)

mn = min(answer)
a = answer.index(mn) +1
print(a)
