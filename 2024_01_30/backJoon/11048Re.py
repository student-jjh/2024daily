N,M = map(int,input().split())
move = [(1,0),(0,1)]

graph = []

for _ in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)

for i in range(1,N):
    graph[i][0] = graph[i-1][0] + graph[i][0]

for j in range(1,M):
    graph[0][j] = graph[0][j-1] + graph[0][j]

for i in range(1,N):
    for j in range(1,M):
        graph[i][j] = graph[i][j] + max(graph[i-1][j],graph[i][j-1])

print(graph[N-1][M-1])

