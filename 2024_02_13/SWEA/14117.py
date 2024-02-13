import heapq
move = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 100000000
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    routh = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph.append(list(map(int,list(input()))))
    routh[0][0] = 0
    q = []
    heapq.heappush(q,(0,0,0))
    while q:
        dist,i,j = heapq.heappop(q)

        if routh[i][j] < dist:
            continue

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            cost = dist + graph[di][dj]
            if routh[di][dj] > cost:
                routh[di][dj] = cost
                heapq.heappush(q,(cost,di,dj))

    print(f"#{test_case} {routh[N-1][N-1]}")



