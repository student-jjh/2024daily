
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    graph_90 = []
    for i in range(0,N,1):
        temp = []
        for j in range(N-1,-1,-1):
            temp.append(graph[j][i])
        graph_90.append(temp)



    graph_180 = []

    for i in range(N-1,-1,-1):
        temp = []
        for j in range(N-1,-1,-1):
            temp.append(graph[i][j])
        graph_180.append(temp)

    graph_270 = []

    for k in range(N-1,-1,-1):

        temp = []
        for v in range(0,N,1):

            temp.append(graph[v][k])
        graph_270.append(temp)




    print(f"#{test_case}")
    for i in range(N):
        for item in graph_90[i]:
            print(item,end = "")
        print(" ",end = "")
        for item in graph_180[i]:
            print(item,end = "")
        print(" ",end = "")
        for item in graph_270[i]:
            print(item,end = "")
        print()

