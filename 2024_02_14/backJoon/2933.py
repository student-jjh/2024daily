from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
M,N = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,list(input()))))

visited = [[[False for _ in range(N+M+1)]for _ in range(M)]for _ in range(N)]

def bfs(graph,v,visited):
    i,j = v

    visited[i][j][0] = True

    queue = deque()
    queue.append((i,j,0))

    while queue:
        i,j,k = queue.popleft()

        for v in range(4):
            di = i + move[v][0]
            dj = j + move[v][1]

            if di < 0 or di >= N or dj < 0 or dj>=M:
                continue

            if di == N -1 and dj == M -1:
                visited[di][dj][k] = True
                continue

            elif graph[di][dj] == 0 and visited[di][dj][k] == False:
                visited[di][dj][k] = True
                queue.append((di,dj,k))


            elif graph[di][dj] == 1 and visited[di][dj][k+1] == False and k < M+N-1:
                visited[di][dj][k+1] = True
                queue.append((di,dj,k+1))

bfs(graph,(0,0),visited)

for i in range(M+N):
    if visited[N-1][M-1][i] ==True:
        print(i)
        break


