import sys
sys.setrecursionlimit(100000)

move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


visited = [[False for _ in range(M)] for _ in range(N)]

def dfs(graph,v,visited):
    global area
    if graph[v[1]][v[0]] == 1 and visited[v[1]][v[0]] == False:
        visited[v[1]][v[0]] = True
        area +=1

        for k in range(4):
            dx = v[0] + move[k][0]
            dy = v[1] + move[k][1]

            if dx < 0 or dx >= M or dy < 0 or dy >=N :
                continue
            elif graph[dy][dx] != 1 or visited[dy][dx] != False :
                continue


            dfs(graph,(dx,dy),visited)
        return True

    return False
count = 0
for_answer = 0

for i in range(M):
    for j in range(N):
        area = 0
        if graph[j][i] != 1 or visited[j][i] != False:
            continue
        if dfs(graph,(i,j),visited):
            count +=1

            for_answer = max(for_answer,area)

print(count)
print(for_answer)