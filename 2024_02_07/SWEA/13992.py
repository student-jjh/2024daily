INF =10000000

def recur(num):
    global  answer
    global sm
    if sm > answer:
        return

    if num == N:
        sm += graph[lst[-1]][0]
        if sm < answer:
            answer = sm
        sm -=graph[lst[-1]][0]
        return

    for i in range(1,N):
        if visited[i] == False:
            visited[i] = True
            sm += graph[lst[-1]][i]
            lst.append(i)
            recur(num+1)
            visited[i] = False
            lst.pop()
            sm -= graph[lst[-1]][i]



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))
    lst = [0]
    m = N
    answer = INF
    sm = 0
    visited = [False for _ in range(N)]
    recur(1)
    print(f"#{test_case} {answer}")