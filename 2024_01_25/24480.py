import sys
sys.setrecursionlimit(10000)

N,M,R = map(int,input().split())

graph = [[]for _ in range(N+1)]
visited = []
check = [False for _ in range(N+1)]

for _ in range(M):
    start, end = map(int,input().split())

    graph[start].append(end)
    graph[end].append(start)

for i in range(N):
    graph[i].sort(reverse=True)
check[R] =True
visited.append(R)
def dfs(graph,R,check,visited):


    for node in graph[R]:
        if check[node] == False:
            visited.append(node)
            check[node] = True
            dfs(graph,node,check,visited)

dfs(graph,R,check,visited)

