N, M = map(int,input().split())
move = [(0,-1),(-1,0),(0,1),(1,0)]
graph = []

for _ in range(N):
    graph.append(list(input()))

visited = [[False for _ in range(M)]for _ in range(N)]
visited[0][0] = True
dp = [[-1 for _ in range(M)]for _ in range(N)]
answer = 0
def dfs(i,j):
    global answer
    if answer == -1:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ways = 0
    answers = 0
    for k in range(4):
        di = i + move[k][0]*int(graph[i][j])
        dj = j + move[k][1]*int(graph[i][j])

        if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == "H":
            continue

        if visited[di][dj] == True:
            answer = -1
            return 0

        visited[di][dj] = True

        ways = dfs(di,dj)
        answers = max(ways,answers)
        visited[di][dj] = False
    dp[i][j] = answers + 1
    if ways == 0:
        return 1
    return dp[i][j]

for_answer = dfs(0,0)

if answer == -1:
    print(-1)

else:
    print(for_answer)
