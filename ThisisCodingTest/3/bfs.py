from collections import deque

def bfs(graph,start,visited):

    visited[start] = True

    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()

        print(v)

        for item in graph[v]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)

