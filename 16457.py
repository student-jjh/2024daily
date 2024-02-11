N,M,K = map(int,input().split())

quests = []

for _ in range(M):
    quests.append(set(map(int,input().split())))

skills = [i for i in range(1,2*N+1)]
visited = [False for _ in range(2*N+1)]
answer = 0
lst = []
def recur(si,num):
    global answer
    if num == N:
        cnt = 0
        
        for quest in quests:
            temp = quest - set(lst)
            if temp == set():
                cnt +=1
        if cnt > answer:
            answer = cnt
    
    for i in range(si,2*N):
        if visited[i] == False:
            visited[i] = True
            lst.append(skills[i])
            recur(i+1,num +1)
            visited[i] = False
            lst.pop()

recur(0,0)
print(answer)
