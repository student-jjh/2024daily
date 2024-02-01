from collections import deque

move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M,K = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

# 낮은 0 밤은 1 k는 벽을 부실 수 있는 횟수 그리고 밤에 기다렸는지 여부까지 확인
def bfs():
    visited = [[K + 1 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0,0,0))
    dn = 0
    answer = 1
    while queue:
        for _ in range(len(queue)):
            i,j,w = queue.popleft()

            if i == N - 1 and j == M - 1:
                return answer
            for m in range(4):
                di = i + move[m][0]
                dj = j + move[m][1]

                if di < 0 or di >=N or dj < 0 or dj >= M or visited[di][dj] <= w:
                    continue

                if graph[di][dj] == 0 :
                    visited[di][dj] = w
                    queue.append((di,dj,w))

                elif w<K:
                    if dn == 0:
                        visited[di][dj] = w +1
                        queue.append((di,dj,w+1))

                    else:
                        queue.append((i, j, w))
        answer +=1
        dn = dn^1
    return -1
print(bfs())