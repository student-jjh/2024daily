from collections import deque
N,M = map(int,input().split())
move = [(1,0),(0,1)]

graph = []
for_answer = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp)


queue = deque()
queue.append((0,0))
for_answer[0][0] = graph[0][0]
answer = []
while queue:
    i,j = queue.popleft()

    for k in range(2):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >=N or dj < 0 or dj >= M:
            continue

        if for_answer[di][dj] < graph[di][dj] + for_answer[i][j] or (graph[di][dj] == 0 and for_answer[di][dj] ==0):
            for_answer[di][dj] = graph[di][dj] + for_answer[i][j]
            queue.append((di,dj))

print(for_answer[N-1][M-1])

