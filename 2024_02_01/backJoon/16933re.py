import heapq
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M,K = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input())))



# 낮은 0 밤은 1 k는 벽을 부실 수 있는 횟수 그리고 밤에 기다렸는지 여부까지 확인
def bfs():
    visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    queue = []
    heapq.heappush(queue,[0,0,0,0,0])

    while queue:
        w,i,j,k,dn = heapq.heappop(queue)
        if i == N-1 and j == M -1:
            return visited[di][dj][k]


        for m in range(4):
            di = i + move[m][0]
            dj = j + move[m][1]

            if di < 0 or di >=N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0 and visited[di][dj][k] == 0:
                visited[di][dj][k] = visited[i][j][k] +1
                heapq.heappush(queue,(visited[di][dj][k],di,dj,k,dn^1))

            elif graph[di][dj] == 1 and k < K:
                if dn == 0:
                    if visited[di][dj][k+1] == 0:
                        visited[di][dj][k+1] = visited[i][j][k] +1
                        heapq.heappush(queue,(visited[di][dj][k+1],di,dj,k+1,dn^1))

                elif dn == 1:
                    if visited[di][dj][k + 1] == 0:
                        visited[di][dj][k + 1] = visited[i][j][k] + 2
                        heapq.heappush(queue,(visited[di][dj][k + 1],di,dj,k+1,dn))

    return -1
print(bfs())