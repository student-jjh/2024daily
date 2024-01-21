import sys
sys.setrecursionlimit(10000)

N = int(input())

graph = []
graph_unnomal = []
visited_nomal = [[False for _ in range(N+1)] for _ in range(N+1)]
visited_unnomal = [[False for _ in range(N+1)] for _ in range(N+1)]

move = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(N):
    temp = list(input())
    temp_unnomal = []
    for item in temp:
        temp_item = item.replace("R","G")
        temp_unnomal.append(temp_item)
    graph.append(temp)
    graph_unnomal.append(temp_unnomal)


def dcf_nomal(graph,v,visited,color):
    
    x,y = v

    if visited[x][y] == False and graph[x][y] == color:

        visited[x][y] = True

        for i in range(4):

            dx = x + move[i][0]
            dy = y + move[i][1]

            if dx < 0 or dx >=N or dy < 0 or dy >=N:
                continue

            dcf_nomal(graph,(dx,dy),visited,color)

        return True

    return False    



count = 0

for i in range(N):
    for j in range(N):
        if dcf_nomal(graph,(i,j),visited_nomal,graph[i][j]) == True:
            count+=1

print(count)

count_ = 0

for i in range(N):
    for j in range(N):
        if dcf_nomal(graph_unnomal,(i,j),visited_unnomal,graph_unnomal[i][j]) == True:
            count_+=1

print(count_)