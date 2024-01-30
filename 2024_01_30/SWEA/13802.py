def dfs(graph,start,visited):
    v = start
    visited[start] = True

    for node in graph[v]:
        if visited[node] == False:
            visited[node] = True
            dfs(graph,node,visited)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    T,M = map(int,input().split())

    graph = [[] for _ in range(100)]
    visited = [False for _ in range(100)]

    temp = list(map(int,input().split()))

    for i in range(0,M*2,2):

        graph[temp[i]].append(temp[i+1])

    dfs(graph,0,visited)


    if visited[99] == True:
        print(f"#{test_case} 1")

    else:
        print(f"#{test_case} 0")