from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())

graph = []
change_graph = []
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int,input().split())))

for _ in range(N):
    change_graph.append(list(map(int,input().split())))

def bfs(graph,change_graph,v,visited):

    i,j = v
    visited[i][j] = True
    change_check = change_graph[i][j]

    queue = deque()
    queue.append((i,j))

    while queue:

        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >=M:
                continue

            if visited[di][dj] == False and graph[di][dj] == graph[i][j]:
                if change_graph[di][dj] != change_check:
                    return "NO"

                else:
                    visited[di][dj] =True
                    queue.append((di,dj))

    return 1
count = 0

if graph == change_graph:
    print("YES")
    exit(0)
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            temp = bfs(graph,change_graph,(i,j),visited)
            if temp == "NO":
                print("NO")
                exit(0)
            else:
                if graph[i][j] != change_graph[i][j]:
                    count +=1

if count == 1:
    print("YES")
else:
    print("NO")




