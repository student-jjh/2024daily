import heapq
big = 1000000000
N,M  = map(int,input().split())

graph = [[] for _ in range(N +1)]
meetcow = [big for _ in range(N+1)]
for _ in range(M):
    start,end,cow = map(int,input().split())

    graph[start].append((end,cow))
    graph[end].append((start,cow))

def dijkstra(start):
    q = []

    heapq.heappush(q,(0,start))

    while q:

        cow,now = heapq.heappop(q)

        if meetcow[now] < cow:
            continue

        for cows in graph[now]:
            meets = cow + cows[1]

            if meets < meetcow[cows[0]]:
                meetcow[cows[0]] = meets

                heapq.heappush(q,(meets,cows[0]))

dijkstra(1)

print(meetcow[N])
