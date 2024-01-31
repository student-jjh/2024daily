import sys
sys.setrecursionlimit(10000)

N,M = map(int,input().split())

graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v,visited):

    for node in graph[v]:
        if visited[node] == 0:
            visited[node] = visited[v] + 1
            dfs(graph,node,visited)

break_point = True
for i in range(0,N):
    visited = [0 for _ in range(N)]
    visited[i] = 1
    dfs(graph,i,visited)
    print(visited)
    if max(visited) >=5:
        print(1)
        break_point = False
        break
if break_point == True:
    print(0)
