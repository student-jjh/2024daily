N = int(input())

if N > 1022:
    print(-1)

else:
    visited=[False for _ in range(10)]
    def n_M(num,ei):
        global cnt
        global m
        if num == m :
            cnt +=1
            if cnt == N+1:
                print("".join(map(str,answer)))
                exit(0)

        for i in range(0,10,1):

            if visited[i] == False and (answer  == [] or answer[-1] > i):
                visited[i] = True
                answer.append(i)
                n_M(num+1,i)
                visited[i] = False
                answer.pop()
    cnt = 0
    for j in range(1,11):
        m = j
        answer = []
        n_M(0,0)




