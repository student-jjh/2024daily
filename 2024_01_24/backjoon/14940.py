from collections import deque
move = [(1,0),(-1,0),(0,-1),(0,1)]

n,m = map(int,input().split())

graph = []
visited = [[-1 for _ in range(m)] for _ in range(n)]
start = [-1,-1]
for i in range(n):
    temp = list(map(int,input().split()))
    if 2 in temp:
        start=[i,temp.index(2)]
    graph.append(temp)

def bfs(graph,v,visited):
    queue = deque()
    visited[v[0]][v[1]] = 0
    queue.append(v)

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=n  or dj <0 or dj >=m:
                continue

            if visited[di][dj] == -1 and graph[di][dj] == 1:
                visited[di][dj] = visited[i][j] +1
                queue.append((di,dj))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                visited[i][j] = 0


    for i in range(n):
        for j in range(m):
            print(visited[i][j],end = " ")
        print()

bfs(graph,start,visited)