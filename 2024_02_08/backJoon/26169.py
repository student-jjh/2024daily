from collections import deque
move = [(1,0),(0,1),(-1,0),(0,-1)]
graph = []
visited = [[False for _ in range(5)] for _ in range(5)]
for _ in range(5):
    graph.append(list(map(int,input().split())))
cnt = 0
answer = False
i,j = map(int,input().split())
visited[i][j] = True
if graph[i][j] == 1:
    cnt +=1
def dfs(num,v,cnt):
    global answer
    i,j = v
    if answer == True:
        return

    if num == 3:
        if cnt >=2:
            answer = True
        return

    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >=5 or dj < 0 or dj >= 5:
            continue

        if visited[di][dj] == False and graph[di][dj] != -1:
            visited[di][dj] = True
            if graph[di][dj] == 1:
                dfs(num + 1, (di,dj),cnt +1)
            else:
                dfs(num +1 ,(di,dj),cnt)
            visited[di][dj] = False

dfs(0,(i,j),cnt)
if answer:
    print(1)
else:
    print(0)
