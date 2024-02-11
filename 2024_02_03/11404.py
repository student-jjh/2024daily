import heapq
import sys
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())

    graph[a].append((c,b))
np = []



def dijstra(i):
    mp = [INF for _ in range(N+1)]
    q = []
    mp[i] = 0
    heapq.heappush(q,(0,i))

    while q:
        dist,now = heapq.heappop(q)

        if dist > mp[now]:
            continue

        for i in graph[now]:

            cost = dist + i[0]

            if mp[i[1]] > cost:
                mp[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))
    np.append(mp)

for j in range(1,N+1):
    dijstra(j)

for i in range(N):
    for j in range(N+1):
        if np[i][j] == INF:
            np[i][j] = 0

for line in np:
    print(*line[1:])
