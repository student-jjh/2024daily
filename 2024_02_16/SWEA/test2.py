
Test = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, Test + 1):

    N,M,K,T = map(int,input().split())

    graph = [[set() for _ in range(M)]for _ in range(N)]

    for k in range(K):
        t,si,sj,h,w = map(int,input().split())

        for i in range(si,min(si + h,N)):
            for j in range(sj,min(sj + w,M)):
                graph[i][j].add(t)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if len(graph[i][j]) != T+1:
                cnt +=1
    print(f"#{test_case} {cnt}")
