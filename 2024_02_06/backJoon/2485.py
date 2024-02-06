N,L,R,X = map(int,input().split())

questions = list(map(int,input().split()))

def recur(si,num):
    global cnt
    if sum(answer) > R:
        return
    if num == m :
        if L <= sum(answer) <= R and (max(answer)-min(answer)) >= X:
            cnt +=1
        return
    for i in range(si,N):
        if visited[i] == False:
            answer.append(questions[i])
            visited[i] = True
            recur(i+1,num + 1)
            answer.pop()
            visited[i] = False


cnt = 0
answer = []
for i in range(2,N+1):
    visited = [False for _ in range(N)]
    m = i
    recur(0,0)
print(cnt)