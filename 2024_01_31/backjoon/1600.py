from collections import deque


K = int(input())
W, H = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(H)]


move = [[1,0],[-1,0],[0,1],[0,-1]]
h_move = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]
def bfs():
    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0))

    while queue:
        i,j,w = queue.popleft()

        if i == H -1 and j == W-1:
            return visited[i][j][w] -1
        for (y,x) in move:
            di,dj = i+y,j+x
            if  0<=di<H and 0<=dj<W and not graph[di][dj] and not visited[di][dj][w]:
                visited[di][dj][w] = visited[i][j][w] + 1
                queue.append((di,dj,w))
        if w < K:
            for (y,x) in h_move:
                di,dj = i + y , j + x
                if 0<=di<H and 0<=dj<W:
                    if not graph[di][dj]:
                        if not visited[di][dj][w+1]:
                            visited[di][dj][w+1] = visited[i][j][w] + 1
                            queue.append((di,dj,w+1))
    return -1
print(bfs())
