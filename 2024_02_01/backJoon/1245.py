from collections import deque

N,M = map(int,input().split())
move = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
visited = [[False for _ in range(M)] for _ in range(N)]

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    queue = deque()
    queue.append((i,j))
    return_mark = True
    while queue:
        i,j = queue.popleft()
        for k in range(8):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >=M:
                continue

            if graph[di][dj] > graph[i][j]:
                visited[i][j] = True
                return_mark =  False

            elif graph[di][dj] == graph[i][j] and visited[di][dj] == False:
                visited[di][dj] = True
                queue.append((di,dj))

    return return_mark

cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and visited[i][j] == False:
            if bfs(graph,(i,j),visited) == True:
                cnt +=1

print(cnt)