
T = int(input())

move = [(1,0),(-1,0),(0,1),(0,-1)]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for_answer = []
    for i in range(N):
        for j in range(M):
            temp = graph[i][j]

            for k in range(4):
                dx = i + move[k][0]
                dy = j + move[k][1]

                if dx < 0 or dx >= N or dy < 0 or dy >= M:
                    continue

                temp += graph[dx][dy]
            for_answer.append(temp)

    for_answer.sort()

    print(f"#{test_case} {for_answer[-1]}")