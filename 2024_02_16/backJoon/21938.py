from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())


graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
T = int(input())
real_graph = []
for line in graph:
    temp_line = []
    for i in range(0,len(graph[0]),3):
        temp = line[i:i+3]
        if sum(temp) >= T*3:
            temp_line.append(1)
        else:
            temp_line.append(0)
    real_graph.append(temp_line)



def bfs(real_graph,v,visted):
    i,j = v

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if visted[di][dj] == False and real_graph[di][dj] == 1:
                visted[di][dj] = True
                queue.append((di,dj))
cnt = 0
visited = [[False for _ in range(M)]for _ in range(N)]
for i in range(N):
    for j in range(M):
       if real_graph[i][j] == 1 and visited[i][j] == False:
           bfs(real_graph,(i,j),visited)
           cnt +=1
print(cnt)

