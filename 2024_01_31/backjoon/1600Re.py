from collections import deque

K = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]
h_move = [(2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,2),(-1,-2)]

W, H = map(int,input().split())

graph = []
visited = [[-1 for _ in range(W)] for _ in range(H)]

for _ in range(H):
    graph.append(list(map(int,input().split())))

def bfs(graph,v,visited):
    i,j,w = v
    visited[i][j] = 0
    queue = deque()
    queue.append((i,j,w))

    while queue:
        i,j,w = queue.popleft()


        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=H or dj < 0 or dj >= W:
                continue

            if graph[di][dj] == 0 and visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] + 1
                queue.append((di,dj,w))


        if w >= 1:

            for k in range(8):
                di = i + h_move[k][0]
                dj = j + h_move[k][1]

                if di < 0 or di >= H or dj < 0 or dj >= W:
                    continue

                if graph[di][dj] == 0 and visited[di][dj] == -1:
                    visited[di][dj] = visited[i][j] + 1
                    queue.append((di,dj,w-1))



bfs(graph,(0,0,K),visited)
print(visited[H-1][W-1])