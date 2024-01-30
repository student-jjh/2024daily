def dfs_stack(start, end):
    global graph
    global answer
    global V

    visited = [0 for _ in range(V + 1)]
    stack = []

    if not graph[start]:
        return

    visited[start] = 1
    for next_node in graph[start]:
        if next_node == end:
            answer = 1
            return
        stack.append(next_node)

    while stack:
        node = stack.pop()
        if visited[node] == 1:
            continue
        visited[node] = 1

        if not graph[node]:
            continue

        for next_node in graph[node]:
            if next_node == end:
                answer = 1
                return
            stack.append(next_node)

answer = 0
answers= []
graph = [[]for _ in range(V + 1)]
V = 0

T = int(input())

for tc in range(1, T + 1):
    # v : 노드의 개수 e : 간선 수
    V, E = map(int, input().split(" "))


for i in range(E):
    start, end = map(int, input().split(" "))
    graph[start].append(end)
S, G = map(int, input().split(" "))
answer = 0
dfs_stack(S, G)
answers.append(answer)
for i in range(1, T + 1):
    print(f"#{i} {answers[i - 1]}")

