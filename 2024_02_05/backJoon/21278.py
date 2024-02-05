import heapq
import sys
INF = sys.maxsize
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = []
def dijstra(graph,i):
    visited = [INF for _ in range(N+1)]
    q = []
    visited[i] = 0

    heapq.heappush(q,(0,i))

    while q:
        dist,now = heapq.heappop(q)

        if dist > visited[now]:
            continue

        for node in graph[now]:

            cost = visited[now] + 1
            if cost < visited[node]:
                visited[node] = cost
                heapq.heappush(q,(cost,node))
    answer.append(visited[1:])

for i in range(1,N+1):
    dijstra(graph,i)

box = []
ans = INF

def re_min(l1,l2):
    temp = 0
    for i in range(N):
        temp += min(l1[i],l2[i])
    return temp

for i in range(N-1):
    for j in range(i+1,N):
        temp = re_min(answer[i],answer[j]) * 2


        if temp < ans:
            ans = temp
            box = []
            box.append((i,j,temp))

        elif temp == ans:
            box.append((i, j,temp))

box.sort(key = lambda x : x[1])
box.sort()

print(box[0][0]+1,box[0][1]+1,box[0][2])