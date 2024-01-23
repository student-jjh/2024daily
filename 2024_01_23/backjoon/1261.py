from collections import deque
move = [(1,0),(-1,0),(0,-1),(0,1)]
M,N = map(int,input().split())

graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input())))


def bfs(graph,v):
    queue = deque()
    queue.append(v)

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]
            print(di,dj)
            if 0 > di or N <= di or 0 > dj or dj >= M:
                continue

            if graph[di][dj] == 1:
                visited[di][dj] = visited[i][j] +1
                visited[i][j] + 1

            elif visited[di][dj] > visited[i][j] +1:
                visited[di][dj] = visited[i][j] +1



            elif visited[di][dj] == 0:
                visited[di][dj] = visited[i][j]

            queue.append((di, dj))

            print(visited)

bfs(graph,(1,1))