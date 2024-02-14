from collections import deque
N,M,K = map(int,input().split())
move = [(1,0),(0,1)]

def bfs(visited,v):
    i,j = v
    visited[i][j] =1

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(2):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di >= N or dj >=M:
                continue

            if visited[di][dj] == -1:
                visited[di][dj] = visited[i][j] +1
                queue.append((di,dj))

if N+M-1 > K:
    print("NO")

else:
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    bfs(visited,(0,0))
    print("YES")
    for line in visited:
        print(*line)