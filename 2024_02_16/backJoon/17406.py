# 배열 크기, 회전수 입력 받기
N,M,K = map(int,input().split())
# 배열 초기화
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
# 회전 방법 입력 받기
turn = []
for _ in range(K):
    turn.append(list(map(int,input().split())))

############################################################
# 배열을 회전시키는 함수, 방향을 입력 받을 수  있게 만들기 for 되돌리기 연산
def turn_graph(r,c,s,w):
    for S in range(s,-1,-1):
        si,sj = r - S, c - S
        ei,ej = r + S, c + S
        # 시계방향 돌리기
        if w == 0:
            next = graph[si][sj]
            for mj in range(sj,ej):
                temp = graph[si][mj + 1]
                graph[si][mj+1] = next
                next = temp

            for mi in range(si,ei):
                temp = graph[mi +1 ][ej]
                graph[mi +1][ej] = next
                next = temp

            for mj in range(ej,sj, -1):
                temp = graph[ei][mj -1]
                graph[ei][mj - 1] = next
                next = temp

            for mi in range(ei,si,-1):
                temp = graph[mi - 1][sj]
                graph[mi - 1][sj] = next
                next = temp


        # 반시계방향 돌리기
        else:
            next = graph[si][sj]
            for mi in range(si, ei):
                temp = graph[mi + 1][sj]
                graph[mi + 1][sj] = next
                next = temp

            for mj in range(sj,ej):
                temp = graph[ei][mj + 1]
                graph[ei][mj+1] = next
                next = temp

            for mi in range(ei,si,-1):
                temp = graph[mi - 1][ej]
                graph[mi - 1][ej] = next
                next = temp

            for mj in range(ej,sj, -1):
                temp = graph[si][mj -1]
                graph[si][mj - 1] = next
                next = temp

# 배열의 최소합을 돌려주는 함수
def count_min(graph):
    answer = 1000000000
    for line in graph:
        temp = sum(line)
        if temp < answer:
            answer = temp

    return answer
# 회전의 순서 정해서 돌리고 최소 합 구하는 함수
visited = [False for _ in range(K)]
real_answer = 10000000
def recur(num):
    global real_answer
    if num == K:
        temp = count_min(graph)
        if temp <real_answer:
            real_answer = temp

    for i in range(K):
        if visited[i] == False:
            visited[i] = True
            r,c,s = turn[i]
            turn_graph(r-1,c-1,s,0)
            recur(num + 1)
            visited[i] = False
            turn_graph(r-1,c-1,s,1)
recur(0)
print(real_answer)
# turn_graph(2,3,2,0)
# for line in graph:
#     print(line)