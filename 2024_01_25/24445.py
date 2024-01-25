from collections import deque

from collections import deque

N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for i in range(N):
    graph[i].sort(reverse=True)

cnt =0
def bfs(graph,v,visited):
    global cnt
    cnt +=1
    visited[v] = cnt

    queue = deque()
    queue.append(v)

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if visited[node] == 0:
                cnt +=1
                visited[node] = cnt
                queue.append(node)
bfs(graph,R,visited)
for i in visited[1:]:
    print(i)