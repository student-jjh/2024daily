from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 0
    while queue:

        i,j = queue.pop()

        if i == N-1 and j == M-1 :
            return count
        
        if i + 1 < N and graph[i+1][j] == 1:
            queue.append((i+1,j))
            graph[i+1][j] = 0

        if j + 1 < M and graph[i][j+1] == 1:         
            queue.append((i,j+1))
            graph[i][j+1] = 0

        count +=1
    
N,M = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

x,y = 0,0

print(bfs(x,y))



