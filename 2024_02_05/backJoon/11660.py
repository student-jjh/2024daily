import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(1,N):
        graph[i][j] += graph[i][j-1]

temp = []
for _ in range(M):
    temp.append(list(map(int,input().split())))

for y1,x1,y2,x2 in temp:
    answer = 0
    for i in range(y1-1,y2):
        if x1 -2 >=0:
            answer+= (graph[i][x2-1] - graph[i][x1-2])
        else:
            answer += graph[i][x2 - 1]
    print(answer)