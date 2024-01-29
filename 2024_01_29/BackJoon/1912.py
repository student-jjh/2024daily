N = int(input())

graph = list(map(int,input().split()))


mm = graph[0]
now = graph[0]

for i in range(1,len(graph)):
    if now > 0:
        now = now + graph[i]
    else:
        now = graph[i]

    if now > mm:
        mm = now

print(mm)
