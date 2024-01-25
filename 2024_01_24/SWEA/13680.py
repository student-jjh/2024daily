T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N ,K = map(int,input().split())

    graph = []
    for_check = 0
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    for i in range(N):
        cnt = 0

        for space in graph[i]:
            if space == 1:
                cnt +=1

            else:
                if cnt == K :
                    for_check +=1
                cnt = 0
        if cnt == K:
            for_check +=1

    temp_graph = list(zip(*graph))

    for i in range(N):
        cnt = 0

        for j in range(N):
            if temp_graph[i][j] == 1:
                cnt += 1

            else:
                if cnt == K:
                    for_check += 1
                cnt = 0
        if cnt == K:
            for_check +=1

    print(f"#{test_case} {for_check}")