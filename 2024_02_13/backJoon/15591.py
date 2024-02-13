import heapq
import sys
INF = sys.maxsize
dic = {}


N, Q = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijistra(graph,v):
    visited = [False for _ in range(N+1)]
    visited[v] = True
    dist = [INF for _ in range(N+1)]
    q = []
    dist[v] = 0
    for di, node in graph[v]:
        visited[node] = True
        dist[node] = di
        heapq.heappush(q,(di,node))

    while q:
        cost,now = heapq.heappop(q)

        if dist[now] < cost:
            continue

        for di,node in graph[now]:
            if visited[node] == False:
                if di <= cost:
                    dist[node] = di
                    heapq.heappush(q,(di,node))
                else:
                    dist[node] = cost
                    heapq.heappush(q,(cost,node))
                visited[node] = True
    dic[str(v)] = dist[1:]

for _ in range(Q):
    K,start = map(int,input().split())

    if str(start) not in dic:
        dijistra(graph,start)
    cnt = 0
    for cost in dic[str(start)]:
        if cost >=K:
            cnt +=1

    print(cnt)












