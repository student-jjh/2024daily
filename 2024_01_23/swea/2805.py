T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    graph = []
    m = (N -1) //2
    for i in range(N):
        temp = list(map(str,input()))
        graph.append(list(map(int,temp)))
    sm = 0
    for i in range(N):
        sm += sum(graph[i])

    for i in range(0,m):
        for j in range(m-i-1,-1,-1):
            answer += graph[i][j]

        for k in range(m+i+1,N):
            answer += graph[i][k]

    for b in range(m+1,N):
        for z in range(b-m):
            answer+= graph[b][z]

        for w in range(b-m):
            answer += graph[b][-w-1]



    print(f"#{test_case} {sm - answer}")