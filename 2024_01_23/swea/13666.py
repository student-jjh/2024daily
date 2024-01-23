move = [(1,0),(-1,0),(0,1),(0,-1)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for_answer = [[0 for _ in range(N)] for _ in range(N)]
    to_add = 0
    for i in range(N):
        for j in range(N):

            temp = graph[i][j]

            for k in range(4):
                dx = i + move[k][0]
                dy = j + move[k][1]

                if dx < 0 or dx >=N  or dy <0 or dy >=N:
                    continue

                to_add += abs(temp - graph[dx][dy])

            for_answer[i][j] = to_add


    print(f"#{test_case} {to_add}")



