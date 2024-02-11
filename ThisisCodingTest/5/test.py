N = int(input())

graph = list(map(int,input().split()))
# graph.reverse()

d = [[x] for x in graph]


for i in range(1,N):
    for j in range(0,i):
        if graph[i] > graph[j] and len(d[i]) < len(d[j]) +1:
            d[i] = []
            d[i].extend(d[j])
            d[i].append(graph[i])

d.sort(key = lambda x : len(x))
print(len(d[-1]))
for item in d[-1]:
    print(item,end = " ")