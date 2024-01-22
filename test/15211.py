move = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(graph,v,visited):
    x,y = v
    global answer

    if visited[x][y] == False:
        visited[x][y] = True

        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]

            if dx < 0 or dx >=16 or dy <0 or dy >=16:
                continue

            if graph[dx][dy] == 3:
                answer = 1
            elif graph[dx][dy] == 0 and visited[dx][dy] == False:
                visited[x][y] = True
                dfs(graph,(dx,dy),visited)



T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    visited = [[False for _ in range(17)] for _ in range(17)]

    for k in range(16):
        temp = list(map(int, input()))
        if 2 in temp:
            y = temp.index((2))
            x = k
        graph.append(temp)

    dfs(graph,(x,y),visited)
    print(f"#{test_case} {answer}")