N,M = map(int,input().split())
answer = []
visited = [False for _ in range(N+1)]
def recur(num,si):
    if num ==M:
        print(*answer)
        return

    for i in range(si,N+1):
        if visited[i] == False:
            answer.append(i)
            visited[i] = True
            recur(num+1,i)
            visited[i] = False
            answer.pop()

recur(0,1)