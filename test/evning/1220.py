from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

move = [0,(1,0),(-1,0)]

for test_case in range(1, T + 1):

    N = int(input())

    graph = []
    stop = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    queue=deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                queue.append((i,j,graph[i][j]))
    count = 0
    while queue:
        x,y,ma = queue.popleft()

        dx = x + move[ma][0]

        if dx < 0 or dx >= N:
            graph[x][y] = 0
            continue

        if graph[dx][y] == 0:
            graph[x][y] = 0
            graph[dx][y] = ma
            queue.append((dx,y,ma))

        if graph[dx][y] != ma:
            stop[dx][y] = True
            if stop[x][y] == False:
                count +=1

        else:
            graph[x][y] = 0

    print(f"{test_case} {count}")