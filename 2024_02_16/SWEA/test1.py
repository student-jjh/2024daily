from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(graph, v, visited):
    i, j = v
    visited[i][j] = 1

    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 1 and visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] + 1
                queue.append((di, dj))
    answer = -2
    for line in visited:
        answer = max(answer, max(line))

    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 지도 행 렬
    N, M = map(int, input().split())
    # 지도 초기화 작업
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    answer = 0
    for_print = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                visited = [[-1 for _ in range(M)] for _ in range(M)]
                temp = bfs(graph, (i, j), visited)
                if answer < temp:
                    answer = temp
                    for_print = []
                    for_print.append((i, j))
                elif answer == temp:
                    for_print.append((i, j))

    for_print.sort(key=lambda x: x[1])
    for_print.sort(key=lambda x: x[0])

    print(f"#{test_case} {for_print[0][0]+1} {for_print[0][1]+1}")