# bfs할꺼니까 임포트
# 0은 호수 1은 배양액을 뿌릴 수 없는 땅 2는 배양액을 뿔리 수 있는 땅
import copy
from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
# 백트레킹으로 배양액을 뿌리는 곳을 변경하면서 BFS로 꽃의 수 count
N,M,G,R = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

# 뿌려진 배양액이 퍼지고, 꽃이 완성되는 괴정 3 = R 4 = G 5 = 꽃
def bfs(graph,lst,visited):
    q = deque(lst)
    cnt = 0
    for i,j in lst:
        visited[i][j] = 0

    while q:
        i,j = q.popleft()
        if graph[i][j] == 5:
            continue

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >= N or dj < 0 or dj >= M:
                continue

            if visited[di][dj] == -1 and (graph[di][dj] == 1 or graph[di][dj] == 2):
                visited[di][dj] = visited[i][j] +1
                graph[di][dj] = graph[i][j]
                q.append((di,dj))

            if visited[di][dj] == visited[i][j] +1 and graph[di][dj] != graph[i][j] and graph[di][dj] != 5:
                graph[di][dj] = 5
                cnt +=1
    return cnt

# 배양액을 뿌릴 수 있는 위치 좌표 확보
lstOfpoint = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            lstOfpoint.append((i,j))

mF = len(lstOfpoint)
check = [False for _ in range(mF)]

# 배양액 수
temp_G = [3 for _ in range(G)]
temp_R = [4 for _ in range(R)]
total = temp_R + temp_G

mP = len(total)

answer = 0
lst = []
def recur(si,num):
    global answer
    if num == mP:
        visited = [[-1 for _ in range(M)] for _ in range(N)]
        temp_graph = copy.deepcopy(graph)
        answer = max(bfs(temp_graph,lst,visited),answer)
        return
    if num < G:
        for i in range(si,mF):
            if check[i] == False:
                lst.append((lstOfpoint[i]))
                graph[lstOfpoint[i][0]][lstOfpoint[i][1]] = temp_G[num]
                check[i] = True
                recur(i+1,num+1)
                lst.pop()
                graph[lstOfpoint[i][0]][lstOfpoint[i][1]] = 2
                check[i] = False
    else:
        if num == G:
            si = 0
        for i in range(si,mF):
            if check[i] == False:
                lst.append((lstOfpoint[i]))
                graph[lstOfpoint[i][0]][lstOfpoint[i][1]] = temp_R[num-G]
                check[i] = True
                recur(i+1,num+1)
                lst.pop()
                graph[lstOfpoint[i][0]][lstOfpoint[i][1]] = 2
                check[i] = False


recur(0,0)
print(answer)



