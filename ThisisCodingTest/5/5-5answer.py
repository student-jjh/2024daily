N = int(input())

graph = list(map(int,input().split()))
# graph.reverse()

d = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if graph[i] > graph[j]:
            d[i] = max(d[i],d[j] +1 )

print(max(d))