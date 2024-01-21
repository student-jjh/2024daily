import sys
sys.setrecursionlimit(10000)

move = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]

def dfs(graph,v,visited):

    x,y = v

    if graph[x][y] == 1 and visited[x][y] == False:

        visited[x][y] = True

        for k in range(8):
            dx = x + move[k][0]
            dy = y + move[k][1]

            if dx < 0 or dx >= h or dy <0 or dy >=w:
                continue

            dfs(graph,(dx,dy),visited)

        return True
    return False


while True:
    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break
    
    graph = []

    for _ in range(h): 
        graph.append(list(map(int,input().split())))

    visited = [[False for q in range(w)] for e in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if dfs(graph,(i,j),visited) == True:
                count +=1

    print(count)
    
