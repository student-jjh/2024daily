from collections import deque

M,N,H = map(int,input().split())
move = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
graph = []
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int,input().split())))

    graph.append(temp)

def bfs(graph,visited,move):
    global M
    global N
    global H
    queue = deque()
    mx = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i,j,k))
                    graph[i][j][k] = 1
    while queue:
        x,y,z = queue.popleft()

        for k in range(6):
            dx = x + move[k][0]
            dy = y + move[k][1]
            dz = z + move[k][2]

            if dx < 0 or dx >= H or dy < 0 or dy >= N or dz <0 or dz >= M:
                continue

            if graph[dx][dy][dz] == 0 and visited[dx][dy][dz] == 0:
                queue.append((dx,dy,dz))
                graph[dx][dy][dz] = 1

                visited[dx][dy][dz] = visited[x][y][z] +1




    for i in range(H):
        for j in range(N):
            if 0 in graph[i][j]:
                return -1
            else:
                mx = max(mx, max(visited[i][j]))

    return mx

print(bfs(graph,visited,move))