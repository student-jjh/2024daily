# 아이디어는 우선 다익스트라로 풀면 될 것 같기는 한데...
# DP로 푸는게 더 적합할 것 같다는 생각이.... .. 왜 아닌지 알았다..
# 다익스트라로 고고
import heapq
import sys
move = [(1,0),(-1,0),(0,1),(0,-1)]
INF = sys.maxsize
def dijstra():
    q = []
    dp[0][0] = graph[0][0]
    heapq.heappush(q,(graph[0][0],0,0))

    while q:
        dist,i,j = heapq.heappop(q)

        if dp[i][j] < dist:
            continue

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj < 0 or dj >=N:
                continue

            cost = dist + graph[di][dj]

            if di == N -1 and dj == N-1:
                return cost


            if cost < dp[di][dj]:
                dp[di][dj] = cost
                heapq.heappush(q,(cost,di,dj))




cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    dp = [[INF for _ in range(N)]for _ in range(N)]

    answer = dijstra()
    print(f"Problem {cnt}: {answer}")
    cnt +=1

