# 아이디어는 송도 맥주축제 그대로..?
from collections import deque

v,m = map(int,input().split())

hole = []
xs,ys = map(float,input().split())
xt,yt = map(float,input().split())

hole.append((xs,ys))

while True:
    try:
        hole.append(tuple(map(float,input().split())))
    except:
        break

hole.append((xt,yt))
visited = [False for _ in range(len(hole))]
visited[0] = True

def is_move(A,B):
    dist = ((A[0]-B[0]) ** 2 + (A[1]-B[1]) ** 2)**0.5
    if dist / (v*60) >= m:
        return False
    return True

def boknal(hole,visited):
    queue = deque()
    queue.append(0)
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            now = queue.popleft()
            if is_move(hole[now], hole[-1]) == True:
                return cnt

            for i in range(len(hole)):
                if visited[i] == False and is_move(hole[now],hole[i]) == True:
                    visited[i] = True
                    queue.append(i)
        cnt +=1
    return -1
temp = boknal(hole,visited)

if temp == -1:
    print("No.")

else:
    print(f"Yes, visiting {temp} other holes.")