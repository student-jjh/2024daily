graph = [0 for _ in range(101)]
graph[1],graph[2],graph[3],graph[4],graph[5],graph[6],graph[7],graph[8],graph[9],graph[10] =1, 1, 1, 2, 2, 3, 4, 5, 7, 9

T = int(input())

for _ in range(T):
    temp = int(input())

    if temp <=10:
        print(graph[temp])

    else:
        for i in range(11,temp+1):
            graph[i] = (graph[i-1]+graph[i-5])

        print(graph[temp])
