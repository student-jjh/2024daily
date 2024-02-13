from collections import deque

def bfs(graph,v,visited):
    visited[v] = 0
    queue = deque()
    queue.append(v)

    while queue:
        now = queue.popleft()

        for node in graph[now]:
            if visited[node] == -1:
                visited[node] = visited[now] + 1
                queue.append(node)



T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 데이터의 길이, 시작점
    N,s = map(int,input().split())
    # 최대 100명 그래프 초기화
    graph = [[] for _ in range(101)]

    # 데이터 입력
    temp = list(map(int,input().split()))

    # 데이터 활용해서 그래프 만들기
    for i in range(0,len(temp),2):
        graph[temp[i]].append(temp[i+1])

    visited = [-1 for _ in range(101)]

    bfs(graph,s,visited)
    mx = max(visited)
    answer = -1
    temp = []
    for i in range(100,-1,-1):
        if visited[i] == mx:
            answer = i
            break

    print(f"#{test_case} {answer}")
