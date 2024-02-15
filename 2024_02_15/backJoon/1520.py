N,M = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]

graph = []
dp = [[-1 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input().split())))

def dfs(i,j):
    if i == N-1 and j == M-1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]
    ways = 0
    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >= N or dj < 0 or dj >= M:
            continue

        if graph[di][dj] < graph[i][j]:
            ways += dfs(di,dj)
    dp[i][j] = ways
    return dp[i][j]

print(dfs(0,0))

