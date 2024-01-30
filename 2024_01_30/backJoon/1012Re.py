T = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    for k in range(4):
        mi = i + move[k][0]
        mj = j + move[k][1]

        if mi < 0 or mi >=N or mj <0 or mj >=M:
            continue

        if graph[mi][mj] == 1 and visited[mi][mj] == False:
            visited[mi][mj] = True
            dfs(graph,(mi,mj),visited)

    return True


for _ in range(T):

    M,N,K = map(int,input().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        j,i = map(int,input().split())
        graph[i][j] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and graph[i][j] == 1:
                dfs(graph,(i,j),visited)
                cnt +=1
    print(cnt)
