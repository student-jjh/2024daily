
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = [[0 for _ in range(10)] for _ in range(10)]

    for _ in range(N):
        x1,y1,x2,y2,c = map(int,input().split())


        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if graph[i][j] == 0:
                    graph[i][j] = c

                elif graph[i][j] == c or graph[i][j] ==3:
                    continue

                else:
                    graph[i][j] += c

    answer = 0

    for line in graph:
        answer += line.count(3)

    print(f'#{test_case} {answer}')
