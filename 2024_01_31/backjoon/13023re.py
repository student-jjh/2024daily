import sys
sys.setrecursionlimit(10000)

N,M = map(int,input().split())

graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v,visited,level):
    global answer
    if level >= 5:
        answer = 1
        return

    for node in graph[v]:
        if visited[node] == False:
            visited[node] = True
            dfs(graph,node,visited,level+1)
            visited[node] = False

break_point = True
answer = 0
for i in range(0,N):
    visited = [False for _ in range(N)]
    visited[i] = True
    dfs(graph,i,visited,1)

print(answer)
