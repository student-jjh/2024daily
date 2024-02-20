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
visited = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == "*":
            q.append((i,j))
            visited[i][j] = 0