from collections import deque
move = [(1,0),(-1,0),(0,1),(0,-1)]
# 지도의 크기 입력받기
R,C = map(int,input().split())

# 지도 초기화
graph = []
# 지도의 각 줄 입력 받기
for _ in range(R):
    graph.append(list(input()))
# 던진 횟수
N = int(input())
# 던지는 높이 (홀수는 왼쪽 짝수는 오른쪽 / 근데 인덱스 상으로는 짝수가 왼쪽 홀수가 오른쪽)
lst = list(map(int,input().split()))
# 클러스터가 떨어지는 함수 구현
def down(graph,cnt,visited):
    temp = []
    for i in range(R):
        for j in range(C):
            if visited[i][j] == cnt:
                temp.append([i,j])

    temp.sort(reverse=True)
    temp = deque(temp)
    break_point = False
    while temp:

        for k in range(len(temp)):
            i,j = temp.popleft()
            di = i +1

            graph[i][j],graph[di][j] = graph[di][j],graph[i][j]
            visited[di][j] = cnt
            visited[i][j] = -1
            temp.append([di,j])


            ddi = di + 1

            if ddi >=R or (graph[ddi][j] == "x" and visited[ddi][j] != cnt):

                break_point = True

        if break_point == True:
            break


# 우선 BFS로 클러스터 구분 부터
def bfs(graph,v,visited,cnt):
    i,j = v
    visited[i][j] = cnt

    queue = deque()
    queue.append((i,j))
    is_fly = True

    while queue:
        i,j = queue.popleft()

        for k in range(4):
            di = i + move[k][0]
            dj = j + move[k][1]

            if di >=R:
                is_fly = False
                continue
            if di < 0  or dj < 0 or dj >=C:
                continue

            if graph[di][dj] == "x" and visited[di][dj] == -1:
                visited[di][dj] = cnt
                queue.append((di,dj))
    if is_fly:
        down(graph,cnt,visited)
# 미네랄 부수기!
for k in range(N):
    if k % 2 == 0:
        for c in range(C):
            if graph[R-lst[k]][c] == "x":
                graph[R - lst[k]][c] = "."
                break
    elif k % 2 == 1:
        for c in range(C-1,-1,-1):
            if graph[R-lst[k]][c] == "x":
                graph[R - lst[k]][c] = "."
                break

    visited = [[-1 for _ in range(C)] for _ in range(R)]
    cnt = 1
    for i in range(R):
        for j in range(C):
            if graph[i][j] == "x" and visited[i][j] == -1:
                bfs(graph,(i,j),visited,cnt)
                cnt +=1



for line in graph:
    print("".join(line))








