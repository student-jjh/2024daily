N,M,K = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = []

for _ in range(N):
    graph.append(list(input()))
visited = [[False for _ in range(M)] for _ in range(N)]
visited[N-1][0] = True
cnt = 0
def dfs(num,i,j):
    global cnt
    if num == K-1:
        if i == 0 and j == M - 1:
            cnt +=1
        return
    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di>=N or dj < 0 or dj >= M:
            continue

        if visited[di][dj] == False and graph[di][dj] != "T":
            visited[di][dj] = True
            dfs(num+1,di,dj)
            visited[di][dj] = False

dfs(0,N-1,0)
print(cnt)