

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(input())
    for_answer = []
    for i in range(1, N, 1):
        for j in range(1, M , 1):
            k = N - i - j
            temp = 0
            if (i + j + k) != N or k < 1:
                continue
            for line in range(i):
                temp += M - graph[line].count("W")
            for line in range(i, i + j):
                temp += M - graph[line].count("B")
            for line in range(i + j, i + j + k):
                temp += M - graph[line].count("R")

            for_answer.append(temp)

    for_answer.sort()

    print(f"#{test_case} {for_answer[0]}")