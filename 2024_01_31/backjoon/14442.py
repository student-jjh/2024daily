from collections import deque

N,M,K = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = []
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(input()))

def bfs_nomal(graph,visited):
    queue = deque()

    i, j, d = 0, 0, 0
    queue.append((i, j, d))
    visited[i][j][d] = 1

    while queue:
        i, j, d = queue.popleft()
        if  i == N-1 and j == M -1:
            return (visited[i][j][d])
        for k in range(4):

            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == '0' and not visited[di][dj][d]:
                visited[di][dj][d] = visited[i][j][d] +1
                queue.append((di,dj,d))

            if graph[di][dj] == '1' and d <K and not visited[di][dj][d+1]:
                visited[di][dj][d+1] = visited[i][j][d] +1
                queue.append((di,dj,d+1))
    return -1

answer = bfs_nomal(graph,visited)
print(answer)