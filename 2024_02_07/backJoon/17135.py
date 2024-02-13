# 아이디어는.. 한칸씩 아래로 이동하는걸 그냥 pop해버리고 싶은데 가능할지.. 일단 트라이

N,M,D = map(int,input().split())

# 두 좌표 사이의 거리를 계산 해줄 함수 미리 구현
def dist(A,B):
    return (abs(A[0]-B[0]) + abs(A[1]-B[1]))

# 적이 배치되어 있는 게임판 초기화
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
# 적의 좌표 모으기
en = []
for i in range(N):
    for j in range(M):
        if graph[i][j] ==1:
            en.append([i,j])


# 궁수 위치 배치를 위한 백트레킹
check = [False for _ in range(N)]
def recur(num):
    if num == 3:
        visited = []
        bfs(graph,visited)


def bfs(graph,vsited):
    pass