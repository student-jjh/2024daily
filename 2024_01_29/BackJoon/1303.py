from collections import deque

move = [(1,0),(-1,0),(0,1),(0,-1)]

M,N = map(int,input().split())

graph = []

B_visited= [[False for _ in range(M)] for _ in range(N)]
W_visited= [[False for _ in range(M)] for _ in range(N)]

B_answer = 0
W_answer = 0

for _ in range(N):
    graph.append(list(input()))

def bfs(graph,v,visited):
    i,j = v

    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    cnt = 1

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj <0 or dj >=M:
                continue

            if graph[di][dj] == graph[i][j] and visited[di][dj] == False:
                visited[di][dj] = True
                cnt +=1
                queue.append((di,dj))
    return cnt

for i in range(N):
    for j in range(M):
        if graph[i][j] =="B" and B_visited[i][j] == False:
            B_answer += (bfs(graph,(i,j),B_visited))**2
        elif graph[i][j] =="W" and W_visited[i][j] == False:
            W_answer += (bfs(graph,(i,j),W_visited))**2


print(W_answer,B_answer)