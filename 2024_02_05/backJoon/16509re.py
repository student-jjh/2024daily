from collections import deque
move = [(2,3),(2,-3),(-2,3),(-2,-3),(3,2),(3,-2),(-3,2),(-3,-2)]
graph = [[0 for _ in range(9)] for _ in range(10)]
visited = [[-1 for _ in range(9)] for _ in range(10)]

i,j = map(int,input().split())

ei,ej = map(int,input().split())
graph[ei][ej] = 1

def bfs(graph,v,visited):
    q = deque()
    i,j = v
    visited[i][j] = 0
    q.append((i,j))

    while q:
        i,j = q.popleft()

        for k in range(8):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= 10 or dj < 0 or dj >= 9:
                continue

            if graph[di][dj] == 1:
                return visited[i][j] +1

            if visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] +1
                q.append((di,dj))

    return -1

print(bfs(graph,(i,j),visited))
