from collections import deque
import sys
input = sys.stdin.readline
move = [(1,0),(-1,0),(0,1),(0,-1)]
R,C = map(int,input().split())

graph = []

def find_all(X):
    if parents[X[0]][X[1]] != [X[0],X[1]]:
        parents[X[0]][X[1]] = find_all(parents[X[0]][X[1]])
    return parents[X[0]][X[1]]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)
    if A==B:
        return
    if A[0] > B[0]:
        parents[B[0]][B[1]] = A
    elif A[0] == B[0]:
        if A[1] > B[1]:
            parents[B[0]][B[1]] = A
        else:
            parents[A[0]][A[1]] = B
    else:
        parents[A[0]][A[1]] = B


parents = [[[] for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        parents[i][j]= [i,j]



for i in range(R):
    graph.append(list(input().rstrip()))

visited=[[False for _ in range(C)]for _ in range(R)]
def bfs(graph,v,visited):
    i,j = v
    visited[i][j] = True

    q = deque()
    q.append((i,j))

    while q:
        i,j = q.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= R or dj < 0 or dj >= C or graph[di][dj] == "X":
                continue

            if visited[di][dj] == False:
                union_all([i,j],[di,dj])
                visited[di][dj] = True
                q.append((di,dj))
for i in range(R):
    for j in range(C):
        if visited[i][j] == False and graph[i][j] !="X":
            bfs(graph,(i,j),visited)

water = [[False for _ in range(C)] for _ in range(R)]
melt = deque()
duck = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == ".":
            water[i][j] = True
        elif graph[i][j] == "L":
            duck.append((i,j))
            water[i][j] = True
        else:
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >= R or dj < 0 or dj >= C or graph[di][dj] == "X":
                    continue
                if graph[di][dj] == "." or graph[di][dj] == "L":
                    melt.append((i,j))
                    break


def melting(graph,melt):
    cnt = 0
    while find_all(duck[0]) != find_all(duck[1]):
        tmp = deque()
        while melt:
            i,j = melt.popleft()
            graph[i][j] = "."

            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >= R or dj < 0 or dj >= C :
                    continue

                if graph[di][dj] != "X":
                    union_all([i,j],[di,dj])

                elif graph[di][dj] == "X" and water[di][dj] == False:
                    water[di][dj] = True
                    tmp.append((di,dj))

        melt = tmp
        cnt +=1
    return cnt
cnt = melting(graph,melt)
print(cnt)






