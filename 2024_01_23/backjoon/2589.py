from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())

graph = []

def return_max(gr):
    temp_mx = 0

    for line in gr:
        temp_mx = max(max(line),temp_mx)

    return temp_mx

for _ in range(N):
    graph.append(list(input()))

def bfs(graph,v):

    visited= [[0 for _ in range(M)] for _ in range(N)]

    i,j = v

    queue = deque()

    queue.append((i,j))

    visited[i][j] = 1

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == "L" and visited[di][dj] == 0:
                visited[di][dj] = visited[i][j] +1
                queue.append((di,dj))

    temp = return_max(visited)
    return temp
mx = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            mx = max(mx,bfs(graph,(i,j)))

print(mx-1)
