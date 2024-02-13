import heapq
INF = 10000000

def dijstra(v):
    visited[v] = 0
    q = []
    heapq.heappush(q,(0,v))

    while q:
        dist,now = heapq.heappop(q)

        if dist > visited[now]:
            continue

        for i in graph[now]:
            cost = dist + i[0]

            if cost < visited[i[1]]:
                visited[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,E = map(int,input().split())

    graph = [[] for _ in range(N)]
    visited = [INF for _ in range(N)]
    for _ in range(E):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))

    dijstra(0)
    print(f"#{test_case} {visited[-1]}")

