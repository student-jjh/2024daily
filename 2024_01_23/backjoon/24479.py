import sys
sys.setrecursionlimit(10000)

N,M,R = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for_answer = [0 for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())

    graph[i].append(j)
    graph[j].append(i)

for i in range(N+1):
    graph[i].sort()

cnt = 0
def dcf(graph,v,visited):
    global cnt
    x = v
    visited[x] = True
    cnt +=1
    for_answer[x] = cnt
    for item in graph[v]:
        if visited[item] == False:
            dcf(graph,item,visited)
dcf(graph,R,visited)
for item in for_answer[1:]:
    print(item)


