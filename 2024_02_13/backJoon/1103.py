N, M = map(int,input().split())
move = [(0,-1),(-1,0),(0,1),(1,0)]
graph = []

for _ in range(N):
    graph.append(list(input()))

visited = [[False for _ in range(M)]for _ in range(N)]
dp = [[-1 for _ in range(M)]for _ in range(N)]
visited[0][0] = True
answer = 0
def dfs(num,graph,visited,v):
    global answer
    if answer == -1:
        return
    if num > answer:
        answer = num
    i,j = v

    for k in range(4):
        di = i + move[k][0]*int(graph[i][j])
        dj = j + move[k][1]*int(graph[i][j])

        if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == "H": continue

        if visited[di][dj] == True:
            answer = -1
            return

        if visited[di][dj] == False:
            if dp[di][dj] != -1:
                return dp[di][dj]
            visited[di][dj] = True
            temp = dfs(num +1,graph,visited,(di,dj))
            visited[di][dj] = False
            if dp[i][j] < temp:
                dp[i][j] = temp
                return temp

    return num


dfs(0,graph,visited,(0,0))
if answer == -1:
    print(-1)
else:
    print(answer+1)