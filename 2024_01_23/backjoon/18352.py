from collections import deque

N,M,K,X = map(int,input().split())
visited = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for_answer = []
for _ in range(M):
    start,end = map(int,input().split())

    graph[start].append(end)
    graph[end].append(end)

queue = deque()
visited[X] = 1
queue.append(X)
while queue:
    now = queue.popleft()

    if visited[now] == K + 1:
        break

    for node in graph[now]:
        if visited[node] == 0:
            visited[node] = visited[now] + 1
            if visited[node] == K +1:
                for_answer.append(node)
            queue.append(node)
for_answer.sort()
if for_answer:
    for item in for_answer:
        print(item)

else:
    print(-1)