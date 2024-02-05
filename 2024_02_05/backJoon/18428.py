import copy
N = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = []

def dfs(graph,stack):
    visited = [[False for _ in range(N)] for _ in range(N)]
    temp_stack = copy.deepcopy(stack)
    while temp_stack:
        i,j = temp_stack.pop()
        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            while True:
                if di < 0 or di >=N or dj <0 or dj>=N:
                    break
                if visited[di][dj] == True:
                    di += move[k][0]
                    dj += move[k][1]
                    continue

                if graph[di][dj] == "S":

                    return False

                elif graph[di][dj] == "O":
                    break

                else:
                    visited[di][dj] = True

                di += move[k][0]
                dj += move[k][1]
    return True

def recur(num):

    if num == 3:
        temp = dfs(graph, stack)
        if temp == True:
            print("YES")
            check = True
            exit(0)

        return
    for i in range(N):
        for j in range(N):
            if tried[i][j] == False and graph[i][j] == "X":
                tried[i][j] = True
                graph[i][j] = "O"
                recur(num+1)
                tried[i][j] = False
                graph[i][j] = "X"

for _ in range(N):
    graph.append(list(map(str,input().split())))

stack = []
tried = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == "T":
            stack.append((i,j))

check = False
recur(0)
if check == False:
    print("NO")