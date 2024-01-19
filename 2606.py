N = int(input())
M = int(input())

visited = [False for j in range(N+1)]
graph = [[] for i in range(N+1)]
count = 0
for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph,v,visited):

    visited[v] = True

    for item in graph[v]:
        if visited[item]==False:
            visited[item] = True
            dfs(graph,item,visited)

    return visited
dfs(graph,1,visited)
print(visited.count(True)-1)