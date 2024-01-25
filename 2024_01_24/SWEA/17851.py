move = [(1,0),(-1,0),(0,1),(0,-1)]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))
    mx = 0
    for i in range(N):
        for j in range(M):
            temp = graph[i][j]
            temp2 = graph[i][j]
            for k in range(4):
                for t in range(1,temp2+1):
                    mi = i + (move[k][0]) * t
                    mj = j + (move[k][1]) * t

                    if mi < 0 or mi >= N or mj < 0 or mj >= M:
                        continue

                    temp += graph[mi][mj]

            mx = max(mx,temp)

    print(f"#{test_case} {mx}")
