# F=건물의 높이
# S= 강호가 있는 층
# G=스타트링크가 있는 층
# U= 위로 버튼을 눌렀을 때 갈 수 있는 층수
# D= 아래로 버튼을 눌렀을 때 갈 수 있는 층수
from collections import deque

F, S, G, U, D = map(int,input().split())


building = [0 for i in range(F+1)]

def bfs(S,G,building):
    building[S] = 1
    queue = deque()
    queue.append(S)

    while queue:
        now = queue.popleft()
        if now == G : break

        if now + U <= F and building[now+U] == 0:
            building[now + U] = building[now] +1
            queue.append(now+U)
        if now - D > 0 and building[now -D] == 0:
            building[now - D] = building[now] +1
            queue.append(now - D)


    if building[G] == 0:
        print("use the stairs")
    else:
        print(building[G]-1)

bfs(S,G,building)