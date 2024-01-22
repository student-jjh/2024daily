from collections import deque


N = int(input())
M = int(input())

prices = [[100001 for _ in range(N+1)] for _ in range(N + 1)]
graph = [[] for i in range(N+1)]

for i in range(M):
    start, end, price = map(int,input().split())
    prices[start][end] = price
    graph[start].append(end)
for_answer = [0 for _ in range(N+1)]


st,ed = map(int,input().split())

def bfs(start,end):

    queue = deque()

    queue.append(start)

    for np in graph[start]:
        for_answer[np] = prices[start][np]

    while queue:

        point = queue.popleft()

        for np in graph[point]:

            if for_answer[point] + prices[point][np] < for_answer[np]:
                for_answer[np] = for_answer[point] + prices[point][np]
            

            else:
                queue.append(np)
    return for_answer[end]
print(bfs(st,ed))