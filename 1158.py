N , K = map(int,input().split())

temp = [i for i in range(N)]
visited = [False for _ in range(N)]
i = K - 1
for_answer = []
for_answer.append(str(temp[i]+1))
visited[i] = True

cnt_print = 1
while cnt_print < N:
    cnt = 0

    while cnt != K:
        i +=1 
        if i >= N:
            i = i % N
        if visited[i] == False:
            cnt +=1


    for_answer.append(str(temp[i]+1)) 
    visited[i] = True
    cnt_print +=1

strtemp = ", ".join(for_answer)
strtemp = "<"+strtemp+">"
print(strtemp)
