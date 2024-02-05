import heapq
import sys
INF = sys.maxsize

N =  int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j] == 1:
            graph[i].append(j)


answer = []
def dijstra(graph,s):
    visited=[INF for _ in range(N)]
    q = []

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
    for i in range(N):
        if visited[i] == INF:
            visited[i] = 0

    for i in range(N):
        if visited[i] >=1:
            visited[i] =1

    answer.append(visited)

for i in range(0,N):
    dijstra(graph,i)

for line in answer:
    print(*line)
