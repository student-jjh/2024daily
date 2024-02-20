real_lst = []
score = [[(1,0,0),(0,0,1)],[(0,1,0),(0,1,0)],[(0,0,1),(1,0,0)]]
for k in range(4):

    lst = []
    temp_lst = list(map(int,input().split()))
    bp = False
    for i in range(0,18,3):
        lst.append(temp_lst[i:i+3])

    real_lst.append(lst)
battle = [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
visited = [[[False for _ in range(3)] for _ in range(6)] for _ in range(6)]
answer = [0,0,0,0]
lt = [[0,0,0] for _ in range(6)]
def recur(num):
    if num == 15:
        if lt in real_lst:
            answer[real_lst.index(lt)] = 1
        return
    i,j = battle[num]
    for v in range(3):

        if visited[i][j][v] == False:

            visited[i][j][v] = True
            lt[i][0] += score[v][0][0]
            lt[i][1] += score[v][0][1]
            lt[i][2] += score[v][0][2]
            lt[j][0] += score[v][1][0]
            lt[j][1] += score[v][1][1]
            lt[j][2] += score[v][1][2]
            recur(num+1)
            visited[i][j][v] = False
            lt[i][0] -= score[v][0][0]
            lt[i][1] -= score[v][0][1]
            lt[i][2] -= score[v][0][2]
            lt[j][0] -= score[v][1][0]
            lt[j][1] -= score[v][1][1]
            lt[j][2] -= score[v][1][2]



recur(0)
print(*answer)