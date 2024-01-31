from collections import deque

def bfs(graph,s,e,visited):
    visited[s] = 0

    queue = deque()
    queue.append(s)

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if node == e:
                return visited[now] +1
            elif visited[node] == -1:
                visited[node] = visited[now] +1
                queue.append(node)
    return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V+1)]
    visited = [-1 for _ in range(V+1)]

    for _ in range(E):
        node_1,node_2 = map(int,input().split())

        graph[node_1].append(node_2)
        graph[node_2].append(node_1)

    S,G = map(int,input().split())

    answer = bfs(graph,S,G,visited)
    print(f"#{test_case} {answer}")

