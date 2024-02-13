from collections import deque
import sys
input = sys.stdin.readline
move = [(1,0),(-1,0),(0,1),(0,-1)]
R,C = map(int,input().split())

parents = [[[] for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        parents[i][j]= [i,j]

water = [[False for _ in range(C)] for _ in range(R)]
visited=[[False for _ in range(C)] for _ in range(R)]
duck = []
melt = deque()

# 그래프 추가하면서 오리 위치 저장하고 오리를 물로 바꾸기
graph = []
for i in range(R):
    temp = list(input().rstrip())
    for j in range(C):
        if temp[j] == "L":
            duck.append([i,j])
            temp[j] = "."
            water[i][j] = True
        elif temp[j] == ".":
            water[i][j] = True
    graph.append(temp)


# 유니온 연산 준비
def find_all(X):
    if parents[X[0]][X[1]] != [X[0],X[1]]:
        parents[X[0]][X[1]] = find_all(parents[X[0]][X[1]])
    return parents[X[0]][X[1]]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)
    if A[0] > B[0]:
        parents[B[0]][B[1]] = A
    elif A[0] == B[0] and A[1] > B[1] :
        parents[B[0]][B[1]] = A
    else:
        parents[A[0]][A[1]] = B
# 유니온 계산 수행하는 작업 그리고 녹을 물 저장해 두는 작업까지 한번에 수행
def bfs(v):
    i,j = v
    visited[i][j] = True
    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=R or dj < 0 or dj >=C:
                continue

            if visited[di][dj] == False and graph[di][dj] == ".":
                visited[di][dj] = True
                union_all([i,j],[di,dj])
                queue.append((di,dj))
            elif water[di][dj] == False and graph[di][dj] == "X":
                water[di][dj] = True
                melt.append((di,dj))

for i in range(R):
    for j in range(C):
        if graph[i][j] == "." and visited[i][j] == False:
            bfs((i,j))


cnt = 0
while find_all(duck[0]) != find_all(duck[1]):

    tmp = deque()
    while melt:
        i,j = melt.popleft()
        graph[i][j] = "."

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= R or dj < 0 or dj >= C:
                continue
            if graph[di][dj] == ".":
                union_all([i,j],[di,dj])

            elif water[di][dj] == False and graph[di][dj] == "X":
                water[di][dj] = True
                tmp.append((di,dj))

    cnt +=1
    melt = tmp
print(cnt)



