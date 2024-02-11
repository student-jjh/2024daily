# 아이디어는 백트레킹에 BFS 섞어서 푸는 문제일듯?
# 5! * 4^^5 그리고 125개 그래프 BFS..? 
from collections import deque
graph  = []
move = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

for _ in range(5):
    temp = []
    for _ in range(5):
        temp.append(list(map(int,input().split())))
    graph.append(temp)

def turn_list(lst,num):
    # 90
    if num == 0:
        temp_lst =[[0 for _ in range(5)]for _ in range(5)]
        for i in range(5):
            for j in range(5):
                temp_lst[j][5-1-i] = lst[i][j]
        return temp_lst
    # 180
    elif num == 1:
        temp_lst =[[0 for _ in range(5)]for _ in range(5)]
        for i in range(5):
            for j in range(5):
                temp_lst[5-1-i][5-1-j] = lst[i][j]
        return temp_lst
    # 270
    elif num == 2:
        temp_lst =[[0 for _ in range(5)]for _ in range(5)]
        for i in range(5):
            for j in range(5):
                temp_lst[5-1-j][i] = lst[i][j]
        return temp_lst
    # 원본
    elif num == 3:
        return lst

# 일단 돌려서 답 찾을 BFS 만들기
def bfs(graph,v,visited):
    z,i,j = v
    visited[z][i][j] = 0
    queue = deque()
    queue.append((z,i,j))
    ez,ei,ej = 4,4,4
    while queue:
        z,i,j = queue.popleft()

        for k in range(6):
            dz = z + move[k][0]
            di = i + move[k][1]
            dj = j + move[k][2]

            if 0 <= dz < 5 and 0 <= di < 5 and 0 <= dj < 5:

                if dz == ez and di == ei and dj == ej:
                    return visited[z][i][j] +1
                
                if visited[dz][di][dj] == -1 and graph[dz][di][dj] == 1:
                    visited[dz][di][dj] = visited[z][i][j] +1
                    queue.append((dz,di,dj))

    return -1
answer = 100000
lst = []
for_check = [False for _ in range(5)]
# 이건 배열 5개 배열 다시해서... (근데 돌리는거 까지 결정을 어떻게 하지?)
def recur(num):
    global answer
    if answer == 12:
        return
    if num == 5:
        temp_graph = []
        for i in lst:
            temp_graph.append(graph[i])
        recur_2(temp_graph,0)
        return

    for k in range(5):
        if for_check[k] == False:
            lst.append(k)
            for_check[k] = True
            recur(num + 1)
            lst.pop()
            for_check[k] = False
lst_2 = []
def recur_2(graph,num):
    global answer
    if answer == 12:
        return
    if num == 5:
        temp_map = []
        for k in range(5):
            temp_map.append(turn_list(graph[k],lst_2[k]))
        if temp_map[0][0][0] == 1 and temp_map[4][4][4] == 1:
            visited = [[[-1 for _ in range(5)]for _ in range(5)] for _ in range(5)] 
            check = bfs(temp_map,(0,0,0),visited)
            if check < answer and check != -1:
                answer = check
        return
    
    for i in range(4):
        lst_2.append(i)
        recur_2(graph,num+1)
        lst_2.pop()


recur(0)
if answer == 100000 :
    print(-1)
else:
    print(answer)


