from collections import deque

moves = [[(0,1),(1,1)],
    [(1,0),(1,1)],
[(0,1),(1,0),(1,1)]]

N = int(input())
graph = []
for _ in range(N):
    graph.append(input().strip().split())



next_status = {(0,1):0,(1,0):1,(1,1):2}

queue = deque()
queue.append((0,1,0))
cnt = 0
while queue:
    i, j, status = queue.popleft()

    for move in moves[status]:
        di = i + move[0]
        dj = j + move[1]



        if di >=N or dj >= N:
            continue

        if move == (1,1):
            if graph[i+1][j] =='1' or graph[i][j] =='1' or graph[i][j+1] == '1' :
                continue

        if graph[di][dj] == '1':
            continue

        if (di,dj) == (N-1,N-1):
            cnt +=1
            break

        future = (di,dj,next_status[move])

        queue.append(future)

print(cnt)






