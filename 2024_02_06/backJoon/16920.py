from collections import deque
import sys
input = sys.stdin.readline

N,M,P = map(int,input().split())
move = [(1,0),(-1,0),(0,1),(0,-1)]
moving = {}

temp = list(map(int,input().split()))
visited = [[False for _ in range(M+1)] for _ in range(N+1)]

for i in range(P):
    moving[str(i+1)] = temp[i]

graph = []
for _ in range(N):
    graph.append(list(input()))

queues = [deque() for _ in range(P+1)]


for i in range(N):
    for j in range(M):
        if graph[i][j] != "." and graph[i][j] != "#":
            queues[int(graph[i][j])].append((i,j))
            visited[i][j] = True

while True:
    move_count = 0
    for v in range(1,P+1):
        move_cnt = 0
        for _ in range(moving[str(v)]):

            for _ in range(len(queues[v])):

                i,j = queues[v].popleft()

                for k in range(4):

                    mi = i + move[k][0]
                    mj = j + move[k][1]

                    if mi < 0 or mi >=N or mj < 0 or mj >= M:
                        continue

                    if visited[mi][mj] == False and graph[mi][mj] == ".":

                        visited[mi][mj] = True
                        graph[mi][mj] = str(v)
                        queues[v].append((mi,mj))
                        move_count +=1
                        move_cnt +=1
            if move_cnt == 0 or not queues[v]:
                break
    if move_count == 0 :
        break

answer = [0 for _ in range(P+1)]

for line in graph:
    for i in range(1,P+1):
        answer[i] += line.count(str(i))

print(*answer[1:])









