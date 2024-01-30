import sys
sys.setrecursionlimit(10000)

T = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(graph,v,visited):

    x,y = v
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]):
        return False

    if graph[x][y] == 1 and visited[x][y] ==False:
        visited[x][y] = True

        for m in range(4):
            mx = x + move[m][0]
            my = y + move[m][1]
            dfs(graph,(mx,my),visited)
        return True
    return False
for i in range(T):
    M,N,K = map(int,input().split())

    graph = [[0 for v in range(M)] for w in range(N)]
    visited = [[False for v in range(M)] for w in range(N)]
    for _ in range(K):
        y,x = map(int,input().split())

        graph[x][y] = 1

    count = 0

    for p in range(N):
        for l in range(M):

            if dfs(graph,(p,l),visited):
                count +=1

    print(count)