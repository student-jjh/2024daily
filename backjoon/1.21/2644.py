from collections import deque

N = int(input())

x,y = map(int,input().split())

m = int(input())

graph = [[] for _ in range(N+1)]

visited =  [0 for _ in range(N+1)]

for _ in range(m):

    _x, _y = map(int,input().split())

    graph[_x].append(_y)
    graph[_y].append(_x)

def bfs(x,y,graph):

    queue = deque()

    queue.append(x)
    visited[x] = 0

    while queue:
        x = queue.popleft()
 
        if y in graph[x]:
            visited[y] = visited[x] + 1
            return visited[y]

        else:
            for i in graph[x]:
                if visited[i] == 0:

                    queue.append(i)
                    visited[i] = visited[x] + 1
                
    return -1


print(bfs(x,y,graph))