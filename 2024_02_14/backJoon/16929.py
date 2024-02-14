N ,M = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
cycle = False
graph = []
visited = [[False for _ in range(M)]for _ in range(N)]
for _ in range(N):
    graph.append(list(input()))

def dfs(graph,v,visited):
    global cycle
    global cnt
    if cycle == True:
        return
    i,j = v
    letter = graph[i][j]

    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >= N or dj < 0 or dj >= M:
            continue

        if graph[di][dj] == letter and visited[di][dj] == False:

            if cnt >= 4:
                for b in range(4):
                    bi = di + move[b][0]
                    bj = dj + move[b][1]

                    if bi < 0 or bi >= N or bj < 0 or bj >= M or (bi == i and bj == j):
                        continue
                    if graph[bi][bj] == letter and visited[bi][bj] == True:
                        cycle = True
                        return
            visited[di][dj] = True
            cnt +=1
            dfs(graph,(di,dj),visited)
            # visited[di][dj] = False

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            cnt = 1
            dfs(graph,(i,j),visited)

        if cycle == True:
            break
    if cycle == True:
        break

if cycle == True:
    print("Yes")
else:
    print("No")

