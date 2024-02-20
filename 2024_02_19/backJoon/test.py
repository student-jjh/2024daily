# 아이디어는 일단 화산을 한바퀴 먼저 돌리고 그 다음부터 화산 사람 순으로 이동하여
# 다음에 확산 될 마그마를 피하는 것이 아닌 그냥 마그마를 피하게 만들자!

from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(graph,visited,s,start):

    queue = deque(s)
    queue.append(start)



    cnt = 0
    while queue:
        for t in range(len(queue)):
            i,j = queue.popleft()

            # 화산 이동 경로 암석지대와 대피소가 아니면 모두 가능
            if graph[i][j] == 3:

                for k in range(4):
                    di = i + move[k][0]
                    dj = j + move[k][1]

                    if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == 0 or graph[di][dj] == 2:
                        continue

                    if visited[di][dj] == False or graph[i][j] == 4:
                        graph[di][dj] = 3
                        visited[di][dj] = True
                        queue.append((di, dj))

            # 사람 이동 경로 땅과 대피소만 갈 수 있음
            elif graph[i][j] == 4:
                for k in range(4):
                    di = i + move[k][0]
                    dj = j + move[k][1]

                    if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == 0 or graph[di][dj] == 3:
                        continue

                    if graph[di][dj] == 2:
                        return cnt +1

                    if visited[di][dj] == False and graph[di][dj] == 1:
                        graph[di][dj] = 4
                        visited[di][dj] = True
                        queue.append((di,dj))


        cnt +=1
    return -1



T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    graph = []

    for i in range(N):
        temp = list(map(int,input().split()))
        if 4 in temp:
            start = (i,temp.index(4))

        graph.append(temp)
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[start[0]][start[1]] = True
    now_3 = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 3:
                now_3.append((i,j))
                visited[i][j] = True
    temp = bfs(graph, visited, now_3, start)
    if temp == -1:
        print("KAKTUS")

    else:
        print(temp)