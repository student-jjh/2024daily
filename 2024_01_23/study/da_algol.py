import sys
import heapq

input = sys.stdin.readline()

INF = int(1e9)

n,m = map(int,input().split())
# 시작 노드 번호 입력
start = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range (N+1)]
distance = [INF for _ in range(N+1)]

for _  in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#이거는 그냥 index 함수랑 min 으로 대체 가능할듯?
def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1,n+1):
        if distance[i] < min_value and not visited:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

def dijkstra_withheap(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        
