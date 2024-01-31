from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,L,R  = map(int,input().split())

graph = []
visited =[[False for _ in range(N)]for _ in range(N)]

def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    queue = deque()
    queue.append((i,j))
    for_cal = set()
    while queue:

        i,j = queue.popleft()

        for k in range(4):

            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj <0 or dj>=N:
                continue

            if visited[di][dj] == False and L<=abs(graph[i][j] -graph[di][dj])<=R:
                queue.append((di,dj))
                visited[di][dj] = True
                for_cal.add((i,j))
                for_cal.add((di,dj))
    return for_cal

for _ in range(N):
    graph.append(list(map(int,input().split())))

while True:
    for i in range(N):
        for_answer = []
        for j in range(N):
            if visited[i][j] == False:
                temp = bfs(graph,(i,j),visited)
                if temp != set():
                    for_answer.append(temp)


