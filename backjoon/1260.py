from collections import deque

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1) ]

def dfs(graph,v,visited):
    
    visited[v] = True
    print(v,end = " ")
    for item in graph[v]:
        if not visited[item]:
            dfs(graph,item,visited)

def bfs(graph,v,visited):

    visited[v] = True
    queue = deque()
    queue.append(v)
    print(v,end = " ")
    while queue:

        i = queue.popleft()

        for item in graph[i]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)
                print(item,end=" ")

for i in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for lists in graph:
    lists.sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(graph,V,visited_dfs)
print()
bfs(graph,V,visited_bfs)