N = int(input())

move = [(1,0),(0,1)]

graph = []

for i in range(N):
    graph.append(list(map(str,input().split())))
for_answer = []
def dfs(graph,v,sr,count):

    i,j = v

    for k in range(2):
        di = i + move[k][0]
        dj = j + move[k][1]

        if 0<= di < N and 0<= dj < N:
            if di == N-1 and dj == N -1:
                temp = eval(sr + graph[di][dj])
                for_answer.append(temp)
            elif count %2 == 0:
                for_sr = sr + graph[di][dj]
                for_sr = eval(for_sr)
                for_sr = str(for_sr)
                dfs(graph, (di, dj), for_sr, count + 1)

            else:
                for_sr = sr +graph[di][dj]
                dfs(graph, (di, dj), for_sr, count + 1)


dfs(graph,(0,0),graph[0][0],1)
print(max(for_answer),min(for_answer))


