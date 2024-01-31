import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
def dfs(graph,start,visited):
    global cnt
    visited[start] = True
    stack.append(start)

    if visited[graph[start]] == True:
        if graph[start] in stack:
            cnt += len(stack[stack.index(graph[start]):])
        else:
            return
    else:
        dfs(graph,graph[start],visited)



for _ in range(T):
    N = int(input().strip())
    visited = [False for _ in range(N+1)]
    graph = [0]
    graph.extend(list(map(int,input().strip().split())))
    cnt = 0
    for i in range(1,N+1):
        if visited[i] == False:
            stack = []
            dfs(graph,i,visited)
    print(N-cnt)