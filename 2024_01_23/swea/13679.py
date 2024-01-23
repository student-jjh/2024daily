

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))
    answer = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for w in range(i,i+M):
                for q in range(j,j+M):
                    temp += graph[w][q]


            answer = max(answer,temp)
    print(f"#{test_case} {answer}")