# 예전에 송도 맥주 축제 처럼 풀면 될듯.? 근데 이번에는 BFS가 아니라 백트레킹으로?

N,M,H = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

lst = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            start = (i,j)
        
        elif graph[i][j] == 2:
            lst.append((i,j))

visited = [False for _ in range(len(lst))]

def possible(v,m):
    for i in range(len(lst)):
        if visited[i] == False:
            if abs(lst[i][0] - v[0]) + abs(lst[i][1] - v[1]) <=m:
                print(v,lst[i],m)
                return True
    return False

answer = 0
def recur(num,v,m):
    global answer
    if answer == len(lst):
        return
    # if possible(v,m) == False:
    if abs(v[0] - start[0]) + abs(v[1] - start[1]) <= m:
        if num > answer:
            answer = num
    
    
    for i in range(len(lst)):
        if visited[i] == False and abs(v[0] - lst[i][0]) + abs(v[1] - lst[i][1]) <= m:
            visited[i] = True
            recur(num+1,(lst[i][0],lst[i][1]),m - (abs(v[0] - lst[i][0]) + abs(v[1] - lst[i][1])) + H)
            visited[i] = False

recur(0,start,M)
print(answer)