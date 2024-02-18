N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))
answer = 0
def recur(num):
    global answer
    if answer == N:
        return
    print(graph,num)
    if num == N:
        cnt = 0
        for i in range(N):
            if graph[i][0] <= 0 :
                cnt +=1
        if cnt > answer:
            answer = cnt
        return

    
    
    if graph[num][0] > 0:
        does = False
        for j in range(N):
            if j != num and graph[j][0] > 0:
                does = True
                graph[num][0] -= graph[j][1]
                graph[j][0] -= graph[num][1]
                recur(num + 1)
                graph[num][0] += graph[j][1]
                graph[j][0] += graph[num][1]
        if does == False:
            recur(num +1)
    else:
        recur(num +1)

recur(0)
print(answer)