from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = True
    graph[i][j] = 2

    queue = deque()
    queue.append((i,j))
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()

            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >= N or dj < 0 or dj >=M:
                    continue

                if visited[di][dj] == False and graph[di][dj] == 1:
                    visited[di][dj] = True
                    graph[di][dj] = graph[i][j] +1
                    queue.append((di,dj))
        cnt +=1
    return cnt

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    si,sj = map(int, input().split())
    graph = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    answer = bfs(graph,(si,sj),visited)
    not_b = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                not_b +=1

    print(f"#{test_case} {answer} {not_b}")
