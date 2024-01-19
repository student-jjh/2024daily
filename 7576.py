from collections import deque

M, N = map(int,input().split())
graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(graph):
    queue = deque()
    for i in range(N):
        for j in range(M):

            if graph[i][j] == 1:

                queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for m in range(4):
            dx = x + move[m][0]
            dy = y + move[m][1]

            if dx <0 or dx >=N or dy < 0 or dy >=M:

                continue
            if graph[dx][dy] == 0:
                graph[dx][dy] = graph[x][y] +1
                queue.append((dx,dy))


    mx = -100
    check = False
    for items in graph:
        if max(items) >  mx:
            mx = max(items)
        if 0 in items:
            check = True
            break
    if check :
        return -1

    elif mx <=1:
        return 0
    else:
        return mx-1

print(bfs(graph))