move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

T = int(input())
def is_omok(graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 'o':
                continue
            else:
                for k in range(8):
                    cnt = 1
                    for v in range(1,5,1):
                        mi = i + ((move[k][0]) * v)
                        mj = j + ((move[k][1]) * v)

                        if mi < 0 or  mi >= N or mj <0 or mj >=N:
                            break

                        if graph[mi][mj] == 'o':
                            cnt += 1

                        else:
                            break

                    if cnt == 5:
                        return "YES"

    return "NO"

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(input())


    print(f"#{test_case} {is_omok(graph)}")


