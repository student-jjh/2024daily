from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = 0

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj <0 or dj >=N:
                continue

            if graph[di][dj] == "3":
                return visited[i][j]

            if graph[di][dj] == "0" and visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] +1
                queue.append((di,dj))

    return 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []
    visitied = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        temp = list(input())

        if "2" in temp:
            start = (i,temp.index("2"))
        graph.append(temp)

    print(f"#{test_case} {bfs(graph,start,visitied)}")





