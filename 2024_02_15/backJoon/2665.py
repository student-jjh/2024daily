from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int,list(input()))))

visited = [[[False for _ in range(N*2-1)] for _ in range(N)]for _ in range(N)]

def bfs(graph,v,visited):
    i,j = v
    visited[i][j][0] = True

    queue = deque()
    queue.append((0,i,j))

    while queue:
        k,i,j = queue.popleft()

        for v in range(4):
            di = i + move[v][0]
            dj = j + move[v][1]

            if di< 0 or di >=N or dj <0 or dj >= N :
                continue

            if di == N-1 and dj ==N-1:
                visited[di][dj][k] = True


            elif graph[di][dj] == 1 and visited[di][dj][k] == False:
                visited[di][dj][k] = True
                queue.append((k,di,dj))

            elif graph[di][dj] == 0 and k < 2*N -2 and visited[di][dj][k+1] == False:
                visited[di][dj][k+1] = True
                queue.append((k+1,di,dj))

bfs(graph,(0,0),visited)
for i in range(2*N -1):
    if visited[N-1][N-1][i] == True:
        print(i)
        break

