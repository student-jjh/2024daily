from collections import deque

moves = [[(0,1),(1,1)],
    [(1,0),(1,1)],
[(0,1),(1,0),(1,1)]]

N = int(input())
graph = []
for _ in range(N):
    graph.append(input().strip().split())
no_visit = {}


next_status = {(0,1):0,(1,0):1,(1,1):2}

queue = deque()
queue.append((0,1,0))
cnt = 0
while queue:
    i, j, status = queue.popleft()
    no = 0
    for move in moves[status]:
        di = i + move[0]
        dj = j + move[1]



        if di >=N or dj >= N:
            no +=1
            continue

        if move == (1,1):
            if graph[i+1][j] =='1' or graph[i][j] =='1' or graph[i][j+1] == '1' :
                no +=1
                continue

        if graph[di][dj] == '1':
            no +=1
            continue

        if (di,dj) == (N-1,N-1):
            cnt +=1
            break

        future = (di,dj,next_status[move])
        if future in no_visit:
            no +=1
            continue
        queue.append(future)
    if no >= len(moves[status]):
        no_visit[(i, j, status)] = 1

print(cnt)