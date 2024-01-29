from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N, K = map(int,input().split())

graph = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

S,X,Y = map(int,input().split())

def bfs(graph,lst,visited,S):
    lst.sort(key = lambda x : x[2])
    queue = deque(lst)


    for i in range(S):

        next_queue = deque()

        while queue:

            i,j,s = queue.popleft()

            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >= N or dj <0 or dj >=N:
                    continue

                if visited[di][dj] == 0:
                    visited[di][dj] = s
                    next_queue.append((di,dj,s))

        queue = next_queue


temp = []

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            temp.append((i,j,graph[i][j]))
            visited[i][j] = graph[i][j]
bfs(graph,temp,visited,S)


print(visited[X-1][Y-1])




