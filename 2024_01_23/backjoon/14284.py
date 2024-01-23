import heapq


N , M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())

    graph[a].append((c,b))
    graph[b].append((c,a))
# list_of_road = []
# graph = [ [] for _ in range(N+1)]
# for _ in range(M):
#     list_of_road.append(list(map(int,input().split())))
price = [1000000 for _ in range(N+1)]
s,t = map(int,input().split())

def dijkstta(start):
    q = []

    heapq.heappush(q,(0,start))

    price[start] = 0

    while q:
        pri,now =heapq.heappop(q)

        if price[now] < pri:
            continue


        for con in graph[now]:
            cost = pri + con[0]

            if cost < price[con[1]]:
                price[con[1]] = cost
                heapq.heappush(q,(cost,con[1]))
# cnt = 0
# while True:
#     price = [1000000 for _ in range(N + 1)]
#     temp = list_of_road[cnt]
#     graph[temp[0]].append((temp[2],temp[1]))
#     graph[temp[1]].append((temp[2],temp[0]))
#     dijkstta(s)
#
#     cnt += 1
#     if price[t] !=1000000 or cnt ==M:
#         break
#
#
# print(price[t])
dijkstta(s)
print(price[t])