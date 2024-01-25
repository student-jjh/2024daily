import sys
input = sys.stdin.readline

N ,M = map(int,input().strip().split())


graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().strip().split())

    graph[b].append(a)

def dfs(graph,v,visited):

    start = v
    visited[start] = True
    for node in graph[start]:
        if visited[node] == False:

            dfs(graph,node,visited)

    return visited.count(True)
for_answer = []
for i in range(1,N+1):
    visited = [False for _ in range(N + 1)]

    cnt = 0
    for_answer.append((i, dfs(graph,i,visited)))

mx = 0

for tu in for_answer:
    if tu[1] > mx:
        mx = tu[1]

for tu in for_answer:
    if tu[1] == mx:
        print(tu[0],end = " ")



