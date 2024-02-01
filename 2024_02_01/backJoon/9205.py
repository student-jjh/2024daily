t = int(input())

def uclid(X,Y):
    if abs(X[0] - Y[0]) + abs(X[1] - Y[1]) <=1000:
        return True
    return False

def dfs(graph,visited,v):
    visited[v] = True

    if uclid(graph[v],graph[-1]):
        visited[-1] = True
        return

    for c in range(len(graph)):
        if visited[c] == False and uclid(graph[v],graph[c]):
            dfs(graph,visited,c)

for _ in range(t):
    n = int(input())
    si,sj = map(int,input().split())

    combin = [[si,sj]]
    for _ in range(n+1):
        combin.append(list(map(int,input().split())))

    visited = [False for _ in range(n+2)]
    dfs(combin,visited,0)
    if visited[-1] == True:
        print("happy")
    else:
        print("sad")

