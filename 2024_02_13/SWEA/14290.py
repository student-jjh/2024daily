
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,E = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    for _ in range(E):
        a,b,c = map(int,input().split())
        graph[a].append((c,b))
        graph[b].append((c,a))

    cnt = 1
    answer = []
    answer.append(0)
    visited[0] = True
    to_print = 0
    while cnt <=N:
        mn = 10000000
        now = N + 1
        for item in answer:
            for dist,node in graph[item]:
                if dist < mn and visited[node] == False:
                    mn,now = dist,node
        visited[now] = True
        answer.append(now)
        to_print += mn
        cnt +=1

    print(f"#{test_case} {to_print}")




