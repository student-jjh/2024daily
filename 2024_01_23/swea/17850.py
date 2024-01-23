move = [(1,0),(-1,0),(0,1),(0,-1)]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    answer = 0

    for i in range(N):
        for j in range(M):
            x,y = i,j
            temp = graph[i][j]
            for k in range(4):
                mx = x+move[k][0]
                my = y+move[k][1]

                if mx < 0 or mx >=N or my <0 or my >=M:
                    continue

                temp += graph[mx][my]


            answer = max(answer,temp)
    print(f'#{test_case} {answer}')