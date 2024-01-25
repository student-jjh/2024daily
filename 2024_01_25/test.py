import copy
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = [[0,0,0,0],
         [0,5,4,0],
         [0,2,1,0],
         [0,3,2,0],
         [0,0,0,0]
         ]

def melting(graph):
    temp_graph = copy.deepcopy(graph)
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                continue
            cnt = 0
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if graph[di][dj] == 0:
                    cnt +=1
            temp_graph[i][j] = max(0,graph[i][j] - cnt)
    return temp_graph

graph = melting(graph)
for line in graph:
    print(line)