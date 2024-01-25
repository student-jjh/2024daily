
move = [(0,1),(0,-1)]
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = input()
    visited= [[False for _ in range(100)] for _ in range(100)]
    graph = []

    for i in range(100):
        graph.append(list(map(int,input().split())))

    idx = graph[99].index(2)

    i,j = 99, idx

    visited[i][j] = True

    while i >0:

        moves = True
        for k in range(2):
            dj = j + move[k][1]

            if dj < 0 or dj >= 100:
                continue
            check = graph[i][dj]
            if graph[i][dj] == 1 and visited[i][dj] == False:

                visited[i][dj] = True
                j = dj
                moves = False
                break
        if moves:
            i -= 1
            visited[i][j] = True


    print(f"#{test_case} {j}")


