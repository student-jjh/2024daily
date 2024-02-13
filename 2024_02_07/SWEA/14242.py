

def recur(num):
    global answer
    global now
    if now < answer :
        return

    if num == N:
        answer = max(answer,now)
        return

    for i in range(N):
        if visited[i] == False:
            if graph[num][i] == 0:
                continue
            now *= graph[num][i]
            visited[i] = True
            recur(num+1)
            now /= graph[num][i]
            visited[i] = False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []
    answer = 0
    now =1
    for _ in range(N):
        temp = [x*0.01 for x in list(map(int,input().split()))]
        graph.append(temp)
    lst = []
    visited = [False for _ in range(N)]

    recur(0)

    print(f"#{test_case} {answer*100:.7f}")