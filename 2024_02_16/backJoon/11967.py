from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())

light = [[False for _ in range(N)] for _ in range(N)]

graph = [[[]for _ in range(N)]for _ in range(N)]

for _ in range(M):
    i,j,ai,aj = map(int,input().split())
    graph[i-1][j-1].append([ai-1,aj-1])

def bfs(graph,v,light):
    global cnt
    global stop_signal
    i,j = v
    visited[i][j] = True
    light[i][j] = True
    queue = deque()
    queue.append((i,j))
    while queue:
        i,j = queue.popleft()

        for ki,kj in graph[i][j]:
            if light[ki][kj] == False:
                light[ki][kj] = True
                stop_signal = False
                cnt +=1

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0  or di >= N or dj < 0 or dj >= N:
                continue

            if visited[di][dj] == False and light[di][dj] == True:
                visited[di][dj] = True
                queue.append((di,dj))

cnt = 1
while True:
    stop_signal = True
    visited = [[False for _ in range(N)] for _ in range(N)]
    bfs(graph,(0,0),light)

    if stop_signal == True:
        break

print(cnt)