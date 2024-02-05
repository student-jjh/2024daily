from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N = int(input())

graph = []
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))
check = []
def bfs_seper(v,graph,visited,cnt):
    i,j = v
    graph[i][j] = cnt
    visited[i][j] = True
    temp = []
    temp.append((i,j))
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            if visited[di][dj] == False and graph[di][dj] == 1:
                graph[di][dj] = cnt
                q.append((di,dj))
                temp.append((di,dj))
    check.append(temp)
cnt = 2
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and graph[i][j] == 1:
            bfs_seper((i,j),graph,visited,cnt)
            cnt +=1

answer = 0

def bfs(graph,visited,lst,cnt):
    for i,j in lst:
        visited[i][j] = 0
    queue = deque(lst)

    while queue:
        i,j = queue.popleft()
        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= N:
                continue

            if graph[di][dj] != 0 and graph[di][dj] != cnt:
                return visited[i][j] +1

            elif graph[di][dj] == 0 and visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] + 1
                queue.append((di, dj))
temp = []
for t in range(2,cnt):
    visiteds = [[-1 for _ in range(N)] for _ in range(N)]
    temp.append(bfs(graph,visiteds,check[t-2],t))

print(min(temp)-1)

