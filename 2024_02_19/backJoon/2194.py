from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]

N,M,A,B,K = map(int,input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    i,j = map(int,input().split())

    graph[i-1][j-1] = 1

si,sj = map(int,input().split())
ei,ej = map(int,input().split())

change_graph = [[0 for _ in range(M-B+1)] for _ in range(N-A+1)]

for i in range(N-A+1):
    for j in range(M-B +1):
        for di in range(i,i+A):
            if 1 in graph[di][j:j+B]:
                change_graph[i][j] = 1
                break
change_graph[si-1][sj-1] = 2
for i in range(ei-1,ei+A-1):
    if 1 in graph[i][ej-1:ej+B-1]:
        print(-1)
        exit(0)
change_graph[ei-1][ej-1] = 3

visited = [[False for _ in range(M-B+1)]for _ in range(N-A+1)]
visited[si-1][sj-1] = True
def bfs(change_graph,v,visited):
    i,j = v

    queue = deque()
    queue.append((i,j))
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            i,j = queue.popleft()

            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >=N-A+1 or dj < 0 or dj >=M-B+1:
                    continue

                if change_graph[di][dj] == 3:
                    return cnt +1

                if change_graph[di][dj] == 0 and visited[di][dj] == False:
                    visited[di][dj] = True
                    queue.append((di,dj))
        cnt +=1
    return -1

print(bfs(change_graph,(si-1,sj-1),visited))

