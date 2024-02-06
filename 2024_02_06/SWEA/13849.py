def recur(num,si):
    global ans
    if num == N:
        answer.append(ans)
        return

    for j in range(N):
        if visited[j] == False:
            visited[j] = True
            ans += graph[si][j]
            recur(num+1,si+1)
            visited[j] = False
            ans -= graph[si][j]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    visited = [False for _ in range(N)]
    graph =  []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    answer = []
    ans = 0
    recur(0,0)
    print(f"#{test_case} {min(answer)}")