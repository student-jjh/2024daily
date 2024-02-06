from collections import deque
move = [(2,3),(2,-3),(-2,3),(-2,-3),(3,2),(3,-2),(-3,2),(-3,-2)]
check = [[(0,1),(1,2)],[(0,-1),(1,-2)],[(0,1),(-1,2)],[(0,-1),(-1,-2)],[(1,0),(2,1)],[(1,0),(2,-1)],[(-1,0),(-2,1)],[(-1,0),(-2,-1)]]
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
            con_p = False
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= 10 or dj < 0 or dj >= 9:
                continue
            for v in range(2):
                ci = i + check[k][v][0]
                cj = j + check[k][v][1]
                if graph[ci][cj] == 1:

                    con_p = True
                    break
            if con_p ==True:
                continue

            if graph[di][dj] == 1:
                return visited[i][j] +1

            if visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] +1
                q.append((di,dj))

    return -1

print(bfs(graph,(i,j),visited))
