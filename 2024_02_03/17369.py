import heapq
import sys
INF = sys.maxsize

N , M = map(int,input().split())

graph = [[] for _ in range(N)]
mp = [INF for _ in range(N)]

sight = list(map(int,input().split()))


for _ in range(M):
    a,b,c = map(int,input().split())

    graph[a].append((c,b))
    graph[b].append((c,a))

for i in range(len(sight)):
    if sight[i] == 1:
        graph[i] = []




def dijstra():

    q = []
    mp[0] = 0
    heapq.heappush(q,(0,0))

    while q:
        dist,now = heapq.heappop(q)

        if dist > mp[now]:
            continue

        for i in graph[now]:

            cost = dist + i[0]

            if mp[i[1]] > cost:
                mp[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

dijstra()
if mp[-1] == INF:
    print(-1)

else:
    print(mp[-1])