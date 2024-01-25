T = int(input())

move = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(graph,v,visited,cnt):
    i,j = v
    visited[i][j] = cnt

    stack = []

    stack.append((i,j))

    while stack:

        i,j = stack.pop()

        for k in range(4):

            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=H or dj < 0 or dj >= W:
                continue

            if graph[di][dj] == "#" and visited[di][dj] == 0:
                visited[di][dj] = cnt
                stack.append((di,dj))


for _ in range(T):
    H, W = map(int,input().split())

    graph = []
    visited = [[0 for _ in range(W)] for _ in range(H)]
    for _ in range(H):
        graph.append(input())
    cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == "#" and visited[i][j] == 0:
                cnt +=1
                dfs(graph,(i,j),visited,cnt)
    mx = 0
    for line in visited:
        mx = max(mx,max(line))

    print(mx)