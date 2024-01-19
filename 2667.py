N = int(input())

graph = []
visited = [[False for i in range(N)] for j in range(N)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
for i in range(N):
    graph.append(list(map(int,input())))


def dfs(graph,N,visited):
    stack = []
    for_answer = []
    for i in range(N):
        for j in range(N):

            if graph[i][j] == 1 and visited[i][j]== False:
                count = 1
                stack.append((i,j))
                visited[i][j] = True

                while stack:
                    x,y = stack.pop()

                    for k in range(4):
                        mx = x+move[k][0]
                        my = y+move[k][1]

                        if mx < 0 or mx >= N or my < 0 or  my >= N:
                            continue

                        if graph[mx][my] == 1 and visited[mx][my] == False:
                            count +=1
                            visited[mx][my] = True
                            stack.append((mx,my))

                for_answer.append(count)
    return for_answer

answer = dfs(graph,N,visited)

answer.sort()
print(len(answer))
for i in answer:
    print(i)