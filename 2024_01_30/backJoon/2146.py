from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

visited= [[-1 for _ in range(N)] for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            visited[i][j] = 0
            queue.append((i,j))

while queue:
    i,j = queue.popleft()

    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >=N or dj < 0 or dj >=N:
            continue

        if graph[di][dj] == 0 and visited[di][dj] == -1:
            visited[di][dj] = visited[i][j] + 1
            queue.append((di,dj))

for line in visited:
    print(line)