from collections import deque

N,M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(graph,v,visited):
    print(v,end=" ")
    visited[v] = 1

    for node in graph[v]:
        if visited[node] == 0:
            dfs(graph,node,visited)

def bfs(graph,v,visited):
    visited[v] = 1
    print(v,end = " ")

    q = deque()
    q.append(v)

    while q:
        now = q.popleft()

        for node in graph[now]:
            if visited[node] == 0:
                visited[node] = 1
                print(node,end = " ")
                q.append(node)


visited_dfs = [0 for _ in range(N+1)]
visited_bfs = [0 for _ in range(N+1)]

dfs(graph,V,visited_dfs)
print()
bfs(graph,V,visited_bfs)