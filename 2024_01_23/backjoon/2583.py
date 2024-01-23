import sys
sys.setrecursionlimit(10000)

M,N,K = map(int,input().split())
move = [(0,1),(0,-1),(1,0),(-1,0)]

graph = [[0 for _ in range(M)] for _ in range(N)]
visited= [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j] = 1

def dcf(graph,v,visited):
    x,y = v
    global area
    if graph[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        area +=1
        for k in range(4):
            mx = x + move[k][0]
            my = y + move[k][1]

            if mx < 0 or mx >= N or my < 0 or my >=M:
                continue
            else:

                dcf(graph,(mx,my),visited)

        return True

    return False
for_answer = []
count = 0
for i in range(N):
    for j in range(M):
        area = 0
        v = (i,j)
        temp = dcf(graph,v,visited)

        if temp:
            count +=1
            for_answer.append(area)
for_answer.sort()
print(count)
for num in for_answer:
    print(num,end = " ")