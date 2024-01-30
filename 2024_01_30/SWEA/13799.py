T = int(input())

def dcf(graph,v,visited):

    visited[v] = True

    stack = []
    stack.append(v)

    while stack:
        now = stack.pop()

        for node in graph[now]:
            if visited[node] == False:
                visited[node] = True
                stack.append(node)


for test_case in range(1, T + 1):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]

    for _ in range(E):

        a, b = map(int,input().split())
        graph[a].append(b)


    S,G = map(int,input().split())

    dcf(graph,S,visited)

    if visited[G] == True:
        print(f"#{test_case} {1}")
    else:
        print(f"#{test_case} {0}")

