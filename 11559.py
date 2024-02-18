# 아이디어는 BFS로 부셔지는거 만들고 나서. 떨어지는거 함수 다시 만들면 될듯?
from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
graph = []

for _ in range(12):
    graph.append(list(input()))

def down_bb(graph):
    break_point = True
    for j in range(6):
        for i in range(11,-1,-1):
            if graph[i][j] != ".":
                for k in range(11,i,-1):
                    if graph[k][j] == ".":
                        graph[i][j],graph[k][j] = graph[k][j],graph[i][j]
                        break_point = False
                        break 
    return break_point
def bfs(graph,v,visited,cnt,check):
    i,j = v
    visited[i][j] = cnt

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(4):

            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=12 or dj < 0 or dj >=6:
                continue

            if graph[di][dj] == graph[i][j] and visited[di][dj] == -1:
                visited[di][dj] = cnt
                check +=1
                queue.append((di,dj))
    return check
answer = 0
while True:
    visited = [[-1 for _ in range(6)] for _ in range(12)]
    cnt = 1
    lst = []
    break_check = True
    for i in range(12):
        for j in range(6):
            if graph[i][j] != "." and visited[i][j] == -1:
                check = 1
                check = bfs(graph,(i,j),visited,cnt,check)
                if check >= 4:
                    lst.append(cnt)
                    break_check = False
                cnt +=1
    
    if lst:
        answer +=1

    while lst:
        now = lst.pop()

        for i in range(12):
            for j in range(6):
                if visited[i][j] == now:
                    graph[i][j] = "."
    

    if break_check == True:
        break
    else:
        temp = down_bb(graph)
        if temp == True:
            break

print(answer)



    

