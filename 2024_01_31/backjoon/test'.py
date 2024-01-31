from collections import deque


k = int(input())
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


dist = [[1,0],[0,1],[-1,0],[0,-1]]
horse = [[2,1],[2,-1],[1,2],[1,-2],[-2,1],[-2,-1],[-1,2],[-1,-2]]

def bfs():
    visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1

    while queue:
        x, y, z = queue.popleft()


        if x==n-1 and y==m-1:
            return visited[x][y][z]-1


        for (i,j) in dist:
            dx, dy = x+i, y+j
            if 0<=dx<n and 0<=dy<m and not visited[dx][dy][z] and not graph[dx][dy]:
                visited[dx][dy][z] = visited[x][y][z]+1
                queue.append([dx,dy,z])


        if z<k:
            for (hi, hj) in horse:
                hx, hy = x+hi, y+hj
                if 0<=hx<n and 0<=hy<m:
                    if not graph[hx][hy]:

                        if not visited[hx][hy][z+1]:
                            visited[hx][hy][z+1] = visited[x][y][z]+1
                            queue.append([hx,hy,z+1])
    return -1


print(bfs())