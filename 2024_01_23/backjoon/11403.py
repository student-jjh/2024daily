from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
answer_graph = []
for i in range(N):
    temp = list(map(int,input().split()))
    answer_graph.append(temp)
    for j in range(len(temp)):
        if temp[j] == 1:
            graph[i].append(j)
            graph[j].append(i)

def dfs(graph,v,for_answer):

    for_answer[v] = True

    print(v)

    for i in graph[v]:
        if visited[i] ==False:
            dfs(graph,i,visited)







