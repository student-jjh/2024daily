N, M = map(int,input().split())
move = [(0,-1),(-1,0),(0,1),(1,0)]
graph = []

for _ in range(N):
    graph.append(list(input()))

visited = [[False for _ in range(M)]for _ in range(N)]
dp = [[-1 for _ in range(M)]for _ in range(N)]
visited[0][0] = True
answer = 0

def dfs(num,i,j):
    global answer
    if answer == -1:
        return -1
    if num > answer:
        answer = num
        if i == 0 and j == 0:
            return answer

    for k in range(4):
        di = i + move[k][0] * int(graph[i][j])
        dj = j + move[k][1] * int(graph[i][j])

        if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == "H": continue

        if visited[di][dj] == True:
            answer = -1
            return

        if visited[di][dj] == False:
            visited[di][dj] = True
            if dp[di][dj] != -1:
                dfs(num+dp[di][dj],0,0)
            
            else:
                dp[di][dj] = dfs(num +1,di,dj)

