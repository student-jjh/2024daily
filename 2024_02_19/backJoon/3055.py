from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]

# 지도 크기
N,M = map(int,input().split())

# 맵 초기화
graph = []

for i in range(N):
    temp = list(input())

    if "S" in temp:
        start = (i,temp.index("S"))

    graph.append(temp)

q = deque()
q.append(start)
visited = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == "*":
            q.append((i,j))
            visited[i][j] = 0


visited[start[0]][start[1]] = 0
def bfs(graph,visited):
    cnt = 0
    while q:

        i,j = q.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if graph[i][j] == "*":
                if graph[di][dj] != "D" and graph[di][dj] !="X" and graph[di][dj] != "*":
                    graph[di][dj] = "*"
                    q.append((di,dj))
                    visited[di][dj] = 0
            else:
                if graph[di][dj] == "D":
                    return visited[i][j] + 1

                if visited[di][dj] == -1 and graph[di][dj] ==".":
                    visited[di][dj] = visited[i][j] + 1
                    q.append((di,dj))
        #
        # print(visited)
        # print(q)
        cnt +=1
    return "KAKTUS"

print(bfs(graph,visited))





