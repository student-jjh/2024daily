# 백트레킹 + BFS 일듯? 시간도 2초고, 512고, 백트레킹도 2개니 가능할듯
from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
# 초기 입력 받고 세팅하는 과정
N,M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))



# BFS
def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    queue = deque()
    queue.append((i,j))
    return_False = False
    cnt = 1
    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di>=N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0:
                return_False = True

            if graph[di][dj] == 2 and visited[di][dj] == False:
                visited[di][dj] = True
                cnt +=1
                queue.append((di,dj))
    if return_False:
        return 0
    else:
        return cnt



answer = 0
# RECUR
def recur(si,num):
    global answer
    if num == 2:
        visited = [[False for _ in range(M)] for _ in range(N)]
        temp = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 2 and visited[i][j] == False:
                    temp += bfs(graph,(i,j),visited)
        if temp > answer:
            answer = temp
        return

    for k in range(si,N*M):
        a = k // M
        b = k % M

        if graph[a][b] == 0:
            graph[a][b] = 1
            recur(k+1,num +1)
            graph[a][b] = 0

recur(0,0)
print(answer)