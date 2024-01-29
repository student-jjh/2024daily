N = int(input())

graph = [0 for _ in range(1001)]

graph[1] = 1
graph[2] = 2

for i in range(3,N+1):
    graph[i] = graph[i-1] + graph[i-2]

print(graph[N]%10007)