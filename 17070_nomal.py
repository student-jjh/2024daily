from collections import deque
import sys
input = sys.stdin.readline

moves = [[[(0,1),(0,1)],[(0,0),(0,0)],[(0,1),(1,1)]],
        [[(0,0),(0,0)],[(1,0),(1,0)],[(1,0),(1,1)]],
        [[(1,1),(0,1)],[(1,1),(1,0)],[(1,1),(1,1)]]]



check = [(1,1),(1,0),(0,1)]

start = [[0,0],[0,1],0]

N = int(input().strip())


graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip().split())))

queue = deque()

queue.append(start)
cnt = 0
while queue:

    now = queue.popleft()
    if now[1] == [N-1,N-1]:
        cnt +=1

    else:
        move = moves[now[2]]

        for i in range(3):
            if i == 0 and now[2] == 1:
                continue
            if i == 1 and now[2] == 0:
                continue

            bi = now[0][0] + move[i][0][0]
            bj = now[0][1] + move[i][0][1]
            fi = now[1][0] + move[i][1][0]
            fj = now[1][1] + move[i][1][1]

            if fi >= N or fj >= N:
                continue

            if i != 2:
                if graph[fi][fj] == 1:
                    continue
            elif i == 2:
                if graph[now[1][0]+1][now[1][1]] == 1 or graph[now[1][0]][now[1][1]+1] == 1 or graph[now[1][0]+1][now[1][1]+1] == 1:
                    continue

            future = [[bi,bj],[fi,fj],i]

            queue.append(future)

print(cnt)