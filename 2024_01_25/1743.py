N,M,K = map(int,input().split())
move = [(0,1),(0,-1),(1,0),(-1,0)]
graph = [[0 for _ in range(M+1)] for _  in range(N+1)]
visited = [[False for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    i,j = map(int,input().split())

    graph[i][j] =1

def dfs(graph,v,visited):
    i,j = v
    cnt = 0
    stack = []
    if graph[i][j] == 1 and visited[i][j] == False:
        visited[i][j] = True
        stack.append((i,j))
        cnt = 1
    while stack:
        i,j = stack.pop()

        for k in range(4):

            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di > N or dj < 0 or dj >M:
                continue

            if graph[di][dj] == 1 and visited[di][dj] == False:
                stack.append((di,dj))
                visited[di][dj] = True
                cnt +=1

    return cnt
mx = 0
for i in range(N+1):
    for j in range(M+1):
        mx = max(mx, dfs(graph,(i,j),visited))
print(mx)
