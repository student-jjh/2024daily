N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))


if N ==1:
    print(graph[0][0])

elif N == 2:
    print(max(graph[0][0] + graph[1][0],graph[0][0] + graph[1][1]))

else:
    graph[1][0] = graph[0][0] + graph[1][0]
    graph[1][1] = graph[0][0] + graph[1][1]

    for i in range(2,N):
        for j in range(len(graph[i])):
            if j == 0 :
                graph[i][j] = graph[i][j] + graph[i-1][0]

            elif j == len(graph[i])-1:
                graph[i][j] = graph[i][j] + graph[i-1][len(graph[i-1])-1]

            else:
                graph[i][j] = graph[i][j] + max(graph[i-1][j-1],graph[i-1][j])

    print(max(graph[-1]))
