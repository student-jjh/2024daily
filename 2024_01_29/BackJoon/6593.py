from collections import deque
while True:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0 :
        break
    move = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    visited= [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    graph = []
    for k in range(L):
        temp = []
        for i in range(R):
            ttemp = list(input())
            if "S" in ttemp:
                v = (k,i,ttemp.index("S"))
            temp.append(ttemp)
        input()
        graph.append(temp)

    def bfs(graph,v,visited):
        k,i,j = v

        visited[k][i][j] = 1

        queue = deque()
        queue.append((k,i,j))
        bk = False
        while queue:
            k,i,j = queue.popleft()

            for b in range(6):

                dk = k + move[b][0]
                di = i + move[b][1]
                dj = j + move[b][2]

                if dk < 0 or dk >= L or di < 0 or di >= R or dj <0 or dj >=C:
                    continue

                if graph[dk][di][dj] == "E":
                    visited[dk][di][dj] = visited[k][i][j] +1
                    return visited[dk][di][dj]

                if graph[dk][di][dj] =="." and visited[dk][di][dj] == 0:
                    visited[dk][di][dj] = visited[k][i][j] +1
                    queue.append((dk,di,dj))


        return -1

    answer=bfs(graph,v,visited)

    if answer == -1:
        print("Trapped!")

    else:
        print(f"Escaped in {answer-1} minute(s).")






