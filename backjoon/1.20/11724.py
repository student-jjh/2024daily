N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited  = [False for _ in range(N+1)]
for i in range(M):
    x,y = map(int,input().split())

    graph[x].append(y)
    graph[y].append(x)

def dfs(graph,v,visited):
    x = v

    if visited[x] == False and graph[x]:
        visited[x] = True

        for y in graph[x]:
            dfs(graph,y,visited)
        
        return True
    return False
result = 0
for i in range(1,N+1):
    if dfs(graph,i,visited) == True:
        result +=1

print(result+visited.count(False))