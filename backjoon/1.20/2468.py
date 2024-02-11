import sys
sys.setrecursionlimit(15000)

N  = int(input())

graph = []
move = [(1,0),(-1,0),(0,1),(0,-1)]
mx = 0
for i in range(N):
    temp = list(map(int,input().split()))
    mx = max(max(temp),mx)

    graph.append(temp)

def dfs(graph,v,visited,n):

    x,y = v

    if graph[x][y] > n and visited[x][y] == False :
        visited[x][y] = True
        for k in range(4):
            mx = x + move[k][0]
            my = y + move[k][1]

            if mx < 0 or mx >=N or my <0 or my >=N:
                continue

            else:
                dfs(graph,(mx,my),visited,n)
        return True

    return False
answer =0
for v in range(mx+1):

    visited = [[False for i in range(N+1)] for j in range(N+1)]

    count = 0
    for i in range(N):
        for j in range(N):
            c = (i,j)
            if dfs(graph,c,visited,v) == True:
                count +=1

    answer = max(count,answer)

print(answer)
