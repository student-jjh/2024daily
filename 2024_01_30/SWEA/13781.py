def dfs(graph,v,visited):

    visited[v] = True
    print(v, end=" ")

    for node in graph[v]:
        if visited[node] == False:
            dfs(graph,node,visited)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]

    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(V+1):
        graph[i].sort()
    print(f"#{test_case}",end = " ")
    dfs(graph,1,visited)
    print()

