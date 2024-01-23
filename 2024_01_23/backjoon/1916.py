import heapq

N = int(input())
M = int(input())
big = 1000010000

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
price = [big for _ in range(N+1)]

for _ in range(M):
    start,end,cost = map(int,input().split())

    graph[start].append((end,cost))

start, end = map(int,input().split())

def dijkstra(start):
    q = []

    price[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        pri,now = heapq.heappop(q)

        if price[now] < pri:
            continue

        for node in graph[now]:
            cost = pri + node[1]

            if cost < price[node[0]]:
                price[node[0]] = cost
                heapq.heappush(q,(cost,node[0]))
dijkstra(start)

print(price[end])