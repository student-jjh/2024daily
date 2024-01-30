from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(graph,lst,visited,person):
    visited[person[0]][person[1]] = 0

    queue = deque(lst)

    while queue:
        i,j,status = queue.popleft()

        if status == "*":
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >=h or dj < 0 or dj >=w:
                    continue
                if graph[di][dj] ==".":
                    graph[di][dj] = "*"
                    queue.append((di,dj,status))
        elif status == "@":
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >=h or dj < 0 or dj >=w:
                    return visited[i][j] +1

                else:
                    if visited[di][dj] == -1 and graph[di][dj] ==".":
                        visited[di][dj] = visited[i][j] +1
                        queue.append((di,dj,status))
    return -1

T = int(input())

for _ in range(T):
    w,h = map(int,input().split())

    graph = []
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    lst = []

    for i in range(h):
        temp = list(input())
        if "@" in temp:
            person = (i,temp.index("@"),"@")

        graph.append(temp)

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                lst.append((i,j,'*'))
    lst.append(person)

    temp = bfs(graph,lst,visited,person)

    if temp == -1:
        print("IMPOSSIBLE")
    else:
        print(temp)
