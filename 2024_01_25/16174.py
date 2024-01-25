N = int(input())
move = [(1,0),(0,1)]

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))


visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(graph,v,visited):
    i,j = v

    visited[i][j] = True

    stack = []
    stack.append((i,j))

    while stack:
        i,j = stack.pop()

        for k in range(2):
            di = i + move[k][0] * graph[i][j]
            dj = j + move[k][1] * graph[i][j]
            if di >= N or dj >= N:
                continue

            if di == N-1 and dj == N-1:
                return True

            if graph[di][dj] != 0 and visited[di][dj] == False:
                visited[di][dj] = True
                stack.append((di,dj))
    return False



if dfs(graph,(0,0),visited):
    print("HaruHaru")

else:
    print("Hing")