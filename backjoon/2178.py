from collections import deque

N, M = map(int,input().split())
graph = []

for i in range(N):
        graph.append(list(map(int,input())))




def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    move = [(-1,0),(1,0),(0,1),(0,-1)]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx >=N or ny <0 or ny >= M:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] +1
                queue.append((nx,ny))



bfs(0,0)
print(graph[N-1][M-1])