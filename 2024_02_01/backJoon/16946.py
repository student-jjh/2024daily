# 처음에 드는 생각은 1000 * 1000 완전 탐색인데... 1트 시작
# bfs니까 deque 가져오기
from collections import deque

# 줄 초기화 N = 세로 M = 가로
N,M = map(int,input().split())

# 움직임 가능성 4방향
move = [(1,0),(-1,0),(0,1),(0,-1)]

# 그래프 입력 받는 부분
graph = []
for_answer = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int,input())))

def bfs(graph,v,visited):

    i,j = v
    visited[i][j] = True
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

            if graph[di][dj] == 0 and visited[di][dj] == False:
                visited[di][dj] = True
                cnt +=1
                queue.append((di,dj))
    return cnt

# 4 방향이 모두 1인 1은 탐색할 필요 X이기 때문에 처리
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited=[[False for _ in range(M)] for _ in range(N)]
            for_answer[i][j] = bfs(graph,(i,j),visited)%10

        else:
            for_answer[i][j] = 0

for line in for_answer:
    for item in line:
        print(item,end ="")
    print()
