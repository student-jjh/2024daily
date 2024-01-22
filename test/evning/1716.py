from copy import deepcopy

def dfs(graph):
    temp_graph = deepcopy(graph)

    stack = []
    conneted = 0
    for i in range(N):
        for j in range(N):
            if temp_graph[i][j] == 1:
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    conneted +=1
                else:
                    stack.append((i,j))
    count = 0
    while stack:

        x,y = stack.pop()
        for k in range(4):
            if k == 0:
                for move in range(x,N):
                    if temp_graph[move][y] == 0:
                        temp_graph[move][y] = 2

                    else:
                        pass
            elif k == 1:
                pass
            elif k == 2:
                pass
            elif k == 3:
                pass
    # for line in temp_graph:
    #     print(line)
    print(stack)
    print(conneted)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    dfs(graph)
