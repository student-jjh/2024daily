from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M,T = map(int,input().split())

def bfs(graph,v,visited):
    i,j,kal = v
    visited[i][j][kal] = 0

    queue = deque()
    queue.append((i,j,kal))

    while queue:
        i,j,kal = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di == N-1 and dj == M-1:
                return visited[i][j][kal] +1

            if di < 0 or di >=N or dj < 0 or dj >=M:
                continue

            if kal == 1 and visited[di][dj][kal] == -1:
                visited[di][dj][kal] = visited[i][j][kal] +1
                queue.append((di,dj,kal))

            else:
                if graph[di][dj] == 0 and visited[di][dj][kal] == -1:
                    visited[di][dj][kal] = visited[i][j][kal] +1
                    queue.append((di,dj,kal))

                elif graph[di][dj] == 2 and visited[di][dj][kal] == -1:
                    visited[i][j][1] = visited[i][j][kal]
                    visited[di][dj][1] = visited[i][j][kal] +1
                    queue.append((di,dj,1))

    return T+1


graph = []
visited = [[[-1] *2 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

temp = bfs(graph,(0,0,0),visited)

if temp > T:
    print("Fail")
else:
    print(temp)