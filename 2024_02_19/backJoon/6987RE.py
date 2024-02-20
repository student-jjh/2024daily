real_lst = []
for k in range(4):

    lst = []
    temp_lst = list(map(int,input().split()))
    bp = False
    for i in range(0,18,3):
        lst.append(temp_lst[i:i+3])

    lst.sort()
    real_lst.append(lst)

visited = [[False for _ in range(6)] for _ in range(6)]
for i in range(6):
    visited[i][i] = True
answer = [0,0,0,0]
lt = [[0,0,0] for _ in range(6)]
def recur(num):
    if num == 15:
        check = lt[:]
        check.sort()
        print(real_lst)
        print(check)
        if check in real_lst:
            answer[real_lst.index(check)] = 1
        return

    for i in range(5):
        for j in range(i + 1, 6):
            if visited[i][j] == False:
                visited[i][j] = True
                visited[j][i] = True
                lt[i][0] +=1
                lt[j][2] +=1
                recur(num+1)
                lt[i][0] -=1
                lt[j][2] -=1

                lt[i][1] +=1
                lt[j][1] +=1
                recur(num+1)
                lt[i][1] -=1
                lt[j][1] -=1

                lt[i][2] +=1
                lt[j][0] +=1
                recur(num+1)
                lt[i][2] -=1
                lt[j][0] -=1

                visited[i][j] = False
                visited[j][i] = False





recur(0)
print(answer)