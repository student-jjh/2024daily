from collections import deque

move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


def bfs(graph,v):
    queue = deque()
    graph[v[0]][v[1]] = 0
    queue.append(v)
    count = 1
    while queue:

        x,y = queue.popleft()

        for k in range(4):
            dx = x + move[k][0]
            dy = y + move[k][1]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            if graph[dx][dy] ==1:
                graph[dx][dy] =0
                queue.append((dx,dy))
                count +=1
    return count
te = []
for i in range(N):
    for j in range(M):
        if graph[i][j] ==1:
            te.append(bfs(graph,(i,j)))


if len(te) == 0 :
    print(len(te))
    print(0)
else:
    print(len(te))
    print(max(te))