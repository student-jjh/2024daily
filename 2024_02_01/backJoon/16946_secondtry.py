# 완전탐색 시간 초과 - > BFS를 0에 활용하는 걸로 2트 시작
# bfs니까 deque 가져오기
from collections import deque

# 줄 초기화 N = 세로 M = 가로
N,M = map(int,input().split())

# 움직임 가능성 4방향
move = [(1,0),(-1,0),(0,1),(0,-1)]
dic = {}
# 그래프 입력 받는 부분
graph = []
for_answer = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input())))
visited=[[0 for _ in range(M)] for _ in range(N)]

def bfs(graph,v,visited,number):

    i,j = v
    visited[i][j] = number
    cnt = 1

    queue = deque()
    queue.append((i,j))

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di < 0 or di >=N or dj < 0 or dj >= M:
                continue

            if graph[di][dj] == 0 and visited[di][dj] == 0:
                visited[di][dj] = number
                cnt +=1
                queue.append((di,dj))
    return cnt
number =1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == 0:

            dic[str(number)] = bfs(graph,(i,j),visited,number)
            number +=1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            check = set()
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >= N or dj < 0 or dj >= M:
                    continue

                if graph[di][dj] == 0:
                    check.add(visited[di][dj])

            answer = 1
            for item in list(check):
                answer += dic[str(item)]

            for_answer[i][j] = answer%10

for line in for_answer:
    for item in line:
        print(item,end ="")
    print()

