N,S = map(int,input().split())

graph = list(map(int,input().split()))

cnt = 0
answer = []
def recur(si,num):
    global cnt
    if num == m:
        if sum(answer) == S:

            cnt +=1
        return

    for i in range(si,N):
        if visited[i] == False:
            answer.append(graph[i])
            visited[i] = True
            recur(i,num+1)
            visited[i] = False
            answer.pop()


for i in range(1,N+1):
    visited = [False for _ in range(N)]
    m = i
    recur(0,0)

print(cnt)