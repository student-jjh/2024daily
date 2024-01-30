move = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >=N or dj <0 or dj >= N:
            continue

        if graph[di][dj] == "3":
            visited[di][dj] = True
            return True

        if graph[di][dj] == "0" and visited[di][dj] == False:
            visited[di][dj] = True
            dfs(graph,(di,dj),visited)




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N =int(input())

    graph = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp = list(input())
        if "3" in temp:
            end = (i,temp.index("3"))
        if "2" in temp:
            start = (i,temp.index("2"))

        graph.append(temp)

    dfs(graph,start,visited)

    if visited[end[0]][end[1]] == True:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")

