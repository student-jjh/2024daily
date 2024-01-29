import heapq
import sys

input = sys.stdin.readline
V,E = map(int,input().strip().split())

K = int(input())

graph = [[] for _ in range(V+1)]
for_answer = [10001 for _ in range(V+1)]
dict = {}

for _ in range(E):
    u,v,w = map(int,input().strip().split())
    if (u,v) in dict:
        if w < dict[(u,v)]:
            dict[(u,v)] = w
    else:
        dict[(u,v)] = w

for routh in dict.items():

    graph[routh[0][0]].append((routh[0][1],routh[1]))


def daijstra(k,graph,for_answer):

    q = []
    heapq.heappush(q,k)
    for_answer[k[0]] = 0

    while q:
        now,w = heapq.heappop(q)

        if w > for_answer[now]:
            continue

        for temp in graph[now]:
            cost = temp[1] + w
            if cost < for_answer[temp[0]]:
                for_answer[temp[0]] = cost
                heapq.heappush(q,(temp[0],cost))

daijstra((K,0),graph,for_answer)

for item in for_answer[1:]:
    if item == 10001:
        print("INF")
    else:
        print(item)