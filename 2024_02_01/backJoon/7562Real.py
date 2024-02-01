from collections import deque
move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

T = int(input())

def bfs(graph,v,e):
    i,j = v
    ei,ej = e
    if i == ei and j ==ej:
        return 0
    graph[i][j] = 1
    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(8):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj <0 or dj >=N:
                continue

            if di == ei and dj == ej:
                return graph[i][j]

            if graph[di][dj] == 0:
                graph[di][dj] = graph[i][j] +1
                queue.append((di,dj))
    return -1

for _ in range(T):
    N = int(input())

    graph = [[0 for _ in range(N)] for _ in range(N)]

    i,j = map(int,input().split())
    ei,ej = map(int,input().split())

    print(bfs(graph,(i,j),(ei,ej)))

