H,W = map(int,input().split())

graph = []
visited = [[-1 for _ in range(W)] for _ in range(H)]


for _ in range(H):
    graph.append(list(input()))

for i in range(H):
    for j in range(W):
        if graph[i][j] == "c":
            visited[i][j] = 0

        elif (j-1) >=0:
            if visited[i][j-1] != -1:
                visited[i][j] = visited[i][j-1] +1
for i in range(H):
    for j in range(W):
        print(visited[i][j], end = " ")
    print()