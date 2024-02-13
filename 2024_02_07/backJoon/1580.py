# 아이디어는 bfs 진행하다가 같은 뎁스에 방문하면...?
#
from collections import deque
N,M = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
graph = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


for i in range(N):
    temp = list(input())
    if "A" in temp:
        A = (0,i,temp.index("A"))
    if "B" in temp:
        B = (1,i,temp.index("B"))
    graph.append(temp)
queue = deque()
queue.append(A)
visited[A[1]][A[2]][0] = 1
queue.append(B)
visited[B[1]][B[2]][1] = 1

def bfs(graph,visited):
    cnt = 0
    answer = 0
    while queue:
        c,i,j = queue.popleft()
        check = False
        for k in range(8):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M or graph[di][dj] == "X":
                continue

            if visited[di][dj][c] == 0:
                if visited[di][dj][c^1] != visited[i][j][c]:
                    if visited[di][dj][c ^ 1] == 1:
                        visited[di][dj][c] = visited[i][j][c] + 1
                    else:
                        visited[di][dj][c] = visited[i][j][c] + 1
                        queue.append((c,di,dj))
                else:
                    check = True
        if check:
            visited[c][i][j] +=1
            queue.append((c, i, j))

    if visited[A[1]][A[2]][A[0]^1] != 0 and  visited[B[1]][B[2]][B[0]^1] != 0 :
        return visited[A[1]][A[2]][A[0]^1] + visited[B[1]][B[2]][B[0]^1]
    return -1



print(bfs(graph,visited))

