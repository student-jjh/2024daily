from collections import deque
import copy

N, M = map(int,input().split())

graphs = []

for _ in range(N):
    graphs.append(list(map(int,input().split())))

move = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    
    queue = deque()
    
    graph = copy.deepcopy(graphs)

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for k in range(4):
            dx = x + move[k][0]
            dy = y + move[k][1]
            if dx < 0 or dx >= N or dy <0 or dy >= M:
                continue
            
            elif graph[dx][dy] == 0:
                graph[dx][dy] = 2
                queue.append((dx,dy))

    global answer 
    count = 0
    for line in graph:
        count += line.count(0)

    answer = max(count,answer)

def make_wall(count):
    if count ==3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graphs[i][j] == 0:
                graphs[i][j] = 1
                make_wall(count+1)
                graphs[i][j] = 0 


answer = 0
make_wall(0)

print(answer)
